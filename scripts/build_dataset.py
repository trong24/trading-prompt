import json, glob, os

SYSTEM_PROMPT_PATH = "templates/master_system_prompt.md"
SYSTEM_PROMPT = open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8").read()

def find_pairs(patterns):
    files = []
    for p in patterns:
        files.extend(glob.glob(p, recursive=True))
    files = sorted(files)
    for f in files:
        if f.endswith(".session.json"):
            out = f.replace(".session.json", ".output.json")
            if os.path.exists(out):
                yield f, out

def to_messages(session_path, output_path):
    user_input = open(session_path, "r", encoding="utf-8").read()
    assistant_out = open(output_path, "r", encoding="utf-8").read()
    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": assistant_out}
        ]
    }

os.makedirs("datasets", exist_ok=True)
output_path = "datasets/train.jsonl"
count = 0

with open(output_path, "w", encoding="utf-8") as fo:
    # Include both sessions and examples (if you store example pairs similarly)
    for s, o in find_pairs(["sessions/**/**.session.json", "examples/**.session.json"]):
        fo.write(json.dumps(to_messages(s, o), ensure_ascii=False) + "\n")
        count += 1

print(f"Wrote {count} examples to {output_path}")
