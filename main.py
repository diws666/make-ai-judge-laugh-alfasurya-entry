import os

LINE = "My boss asked me to think outside the box. I did. Now I am outside the building, and HR wants a word."  # verified: 101 chars

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE.encode("utf-8")))
