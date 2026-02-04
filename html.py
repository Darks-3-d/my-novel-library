import os
import re

# Use absolute paths to avoid "File Not Found" errors
INPUT_FILE = r"C:\Users\ronny\Desktop\website\my-novel-library\content\mount-hua.md"
OUTPUT_DIR = r"C:\Users\ronny\Desktop\website\my-novel-library\content\mount-hua-sect"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

# This regex looks for common chapter patterns like "Chapter 1", "Episode 1", or "##"
# It is more reliable for 1,000+ chapter web novels
chapters = re.split(r'(?i)(?=chapter\s+\d+|episode\s+\d+|##\s+)', text)

count = 0
for chapter in chapters:
    clean_content = chapter.strip()
    if len(clean_content) < 100: # Skip very short snippets or empty breaks
        continue
    
    count += 1
    file_name = f"chapter-{count:04d}.md"
    with open(os.path.join(OUTPUT_DIR, file_name), 'w', encoding='utf-8') as f:
        # Hugo Frontmatter for the clean UI
        f.write(f"---\ntitle: \"Chapter {count}\"\nweight: {count}\n---\n\n")
        f.write(clean_content)

print(f"Successfully split into {count} chapters.")