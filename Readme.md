# BTC Trading Training Repo (Skeleton)

This repository hosts your long-run (>100h) BTC trading training data and prompts. It’s optimized so ChatGPT can read specific files (via GitHub connector) and you can easily build few-shot datasets or fine-tune later.

## Structure
```
btc-trading-training/
├── spec/                        # Your fixed trading spec (rarely changes)
│   ├── trader_spec.yaml         # Style, setups, risk rules, sizing, exits
│   └── risk_management.md       # Human-readable notes
├── context_blocks/              # Definitions, risk guidelines, journaling
│   ├── trading_definitions.md
│   ├── risk_management_guidelines.md
│   └── journaling_prompts.md
├── modules/                     # Modular rules/patterns used in daily analysis
│   ├── module00_mindset_psychology.md
│   ├── module01_risk_and_btc.md
│   ├── module02_signal_and_execution.md
│   ├── module03_mtf.md
│   ├── module04a_rsi_co_ban.md
│   ├── module04b_quan_tinh_rsi.md
│   ├── module04c_mtf_method.md
│   ├── module04d_case_studies.md
│   └── module05_rsi_ma9_wma45_system.md
├── sessions/                    # Ground-truth session logs (INPUT/OUTPUT pairs)
│   └── YYYY/MM/...
├── examples/                    # Small pedagogical examples (optional)
├── datasets/                    # Built JSONL datasets for few-shot/fine-tune
│   ├── train.jsonl
│   └── val.jsonl
├── templates/                   # Master prompt + daily session input template
│   ├── master_system_prompt.md
│   └── session_input_template.json
├── scripts/                     # Utilities (build dataset, validation, etc.)
│   └── build_dataset.py
└── README.md
```

## Quick start
1. Fill `spec/trader_spec.yaml` with your real rules (risk, sizing, setups).
2. Each trading session, create two files under `sessions/YYYY/MM/`:
   - `YYYY-MM-DD_NN.session.json`  (the exact input you provided to the model)
   - `YYYY-MM-DD_NN.output.json`   (the *actual* plan/decision you took — ground truth)
3. Run `python scripts/build_dataset.py` to generate `datasets/train.jsonl` from paired sessions (and from examples if any).
4. Use `templates/master_system_prompt.md` + your `session_input_template.json` to run daily.
5. When ready, upload `datasets/train.jsonl` to your fine-tune pipeline.

> Tip: Keep each session focused and consistent. The model learns best with clean, high-quality INPUT/OUTPUT pairs.
