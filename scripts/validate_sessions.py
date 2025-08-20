#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
from pathlib import Path
from typing import Tuple, List

from jsonschema import Draft7Validator

REPO_ROOT_DEFAULT = Path(__file__).resolve().parents[1]  # repo/

def load_json(p: Path):
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def validate_with_schema(data: dict, schema: dict) -> List[str]:
    validator = Draft7Validator(schema)
    errors = []
    for e in validator.iter_errors(data):
        path = ".".join([str(x) for x in e.path])
        errors.append(f"[schema] {path or '<root>'}: {e.message}")
    return errors

def best_rr(entry: float, stop: float, targets: List[float]) -> float:
    # RR = |target - entry| / |entry - stop|
    denom = abs(entry - stop)
    if denom == 0:
        return 0.0
    return max(abs(t - entry) / denom for t in targets) if targets else 0.0

# --- Hard constraint: Only OKX + BTCUSDT.P + perp ---
OKX_VENUE = "OKX"
OKX_INSTRUMENT = "BTCUSDT.P"
OKX_TYPE = "perp"

def enforce_okx_only(inp: dict) -> List[str]:
    errs = []
    acct = inp.get("account")
    if not isinstance(acct, dict):
        acct = {}
    if acct.get("venue") != OKX_VENUE:
        errs.append(f"[input] account.venue must be '{OKX_VENUE}'")
    if acct.get("instrument") != OKX_INSTRUMENT:
        errs.append(f"[input] account.instrument must be '{OKX_INSTRUMENT}'")
    if acct.get("type") != OKX_TYPE:
        errs.append(f"[input] account.type must be '{OKX_TYPE}'")
    return errs

def domain_checks_input(inp: dict) -> List[str]:
    warns = []
    # NAV > 0
    if not (isinstance(inp.get("nav_usdt"), (int, float)) and inp["nav_usdt"] > 0):
        warns.append("[input] nav_usdt should be > 0")

    # Mode sanity
    mode = inp.get("session", {}).get("mode")
    if mode not in {"scan", "review", "live"}:
        warns.append(f"[input] session.mode unexpected: {mode}")

    # Positions basic check
    for i, pos in enumerate(inp.get("positions", []) or []):
        side = pos.get("side")
        stop = pos.get("stop")
        avg = pos.get("avg_price")
        if side in {"long", "short"} and isinstance(stop, (int, float)) and isinstance(avg, (int, float)):
            if side == "long" and stop >= avg:
                warns.append(f"[input] positions[{i}]: long but stop ({stop}) >= avg_price ({avg})")
            if side == "short" and stop <= avg:
                warns.append(f"[input] positions[{i}]: short but stop ({stop}) <= avg_price ({avg})")
    return warns

def domain_checks_output(out: dict) -> Tuple[List[str], List[str]]:
    warns, errs = [], []
    entry = out.get("entry")
    stop = out.get("stop")
    side = out.get("side")

    # Stop/entry relation
    if isinstance(entry, (int, float)) and isinstance(stop, (int, float)):
        if side == "long" and stop >= entry:
            warns.append(f"[output] long but stop ({stop}) >= entry ({entry})")
        if side == "short" and stop <= entry:
            warns.append(f"[output] short but stop ({stop}) <= entry ({entry})")

    # RR check (if targets provided)
    targets = out.get("targets") or []
    if isinstance(entry, (int, float)) and isinstance(stop, (int, float)) and isinstance(targets, list) and targets:
        rr = best_rr(entry, stop, [t for t in targets if isinstance(t, (int, float))])
        if rr < 2:
            warns.append(f"[output] RR max {rr:.2f} < 2.0")

    # risk_pct soft cap
    rp = out.get("risk_pct")
    if isinstance(rp, (int, float)) and rp > 2.0:
        warns.append(f"[output] risk_pct {rp}% > 2% (spec khuyến nghị)")

    return warns, errs

def find_pairs(root: Path, include_examples: bool) -> List[Tuple[Path, Path]]:
    patterns = [
        "sessions/**/*.session.json",
    ]
    if include_examples:
        patterns.append("examples/**/*.session.json")
    session_files = []
    for pat in patterns:
        session_files.extend(sorted(root.glob(pat)))
    pairs = []
    for s in session_files:
        o = Path(str(s).replace(".session.json", ".output.json"))
        pairs.append((s, o))
    return pairs

def main():
    ap = argparse.ArgumentParser(description="Validate trading sessions against JSON Schemas + domain checks.")
    ap.add_argument("--root", type=Path, default=REPO_ROOT_DEFAULT, help="Repo root (default: scripts/../)")
    ap.add_argument("--strict", action="store_true", help="Treat warnings as errors (non-zero exit).")
    ap.add_argument("--include-examples", action="store_true", help="Also validate examples/**")
    args = ap.parse_args()

    root = args.root.resolve()
    schemas_dir = root / "schemas"
    in_schema = load_json(schemas_dir / "session_input.schema.json")
    out_schema = load_json(schemas_dir / "session_output.schema.json")

    pairs = find_pairs(root, include_examples=args.include_examples)
    if not pairs:
        print("No session files found.")
        return 0

    total_err = 0
    total_warn = 0
    total_ok = 0

    for s_path, o_path in pairs:
        rel_s = s_path.relative_to(root)
        rel_o = o_path.relative_to(root)
        file_errors = []
        file_warns = []

        # existence
        if not s_path.exists():
            file_errors.append(f"[fs] missing input: {rel_s}")
        if not o_path.exists():
            file_errors.append(f"[fs] missing output pair: {rel_o}")

        inp = load_json(s_path) if s_path.exists() else {}
        out = load_json(o_path) if o_path.exists() else {}

        # schema
        file_errors += validate_with_schema(inp, in_schema)
        file_errors += validate_with_schema(out, out_schema)

        # hard constraint: OKX + BTCUSDT.P + perp
        file_errors += enforce_okx_only(inp)

        # domain checks
        file_warns += domain_checks_input(inp)
        w, e = domain_checks_output(out)
        file_warns += w
        file_errors += e

        # summary per file
        if file_errors or file_warns:
            print(f"\n=== {rel_s} / {rel_o} ===")
            for m in file_errors:
                print("ERROR:", m)
            for m in file_warns:
                print("WARN :", m)

        total_err += len(file_errors)
        total_warn += len(file_warns)
        if not file_errors and not file_warns:
            total_ok += 1

    print("\n--- Summary ---")
    print(f"OK: {total_ok} | WARN: {total_warn} | ERR: {total_err}")

    if total_err > 0 or (args.strict and total_warn > 0):
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
