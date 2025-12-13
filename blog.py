from pathlib import Path
import json

blog_dir = Path("blog")
output_path = Path("blog_files.json")

# Find all .txt files
files = sorted(
    [p for p in blog_dir.glob("*.txt")],
    key=lambda p: p.stem,  # '20251212' part of '20251212.txt'
    reverse=True           # newest first
)

# Build list of URLs/paths relative to index.html
file_list = [str(p.as_posix()) for p in files]

output_path.write_text(
    json.dumps(file_list, indent=2),
    encoding="utf-8"
)

print(f"Wrote {output_path} with {len(file_list)} entries.")
