import json
import re
import sys

def correct_and_parse_json_like_content(content):
    corrected_content = re.sub(r'(\w+)(\s*:\s*)', r'"\1"\2', content)
    corrected_content = re.sub(r'(:\s*)([^\d\[\{"\'][\w\s,.]+)([,\]\}])', r'\1"\2"\3', corrected_content)
    return corrected_content

def parse_and_validate_json(data):
    data = correct_and_parse_json_like_content(data)
    pr_data = json.loads(data)
    required_keys = ["Date", "Category", "Title", "Preview", "BusinessValues", "Highlights", "Updates", "Deprecations", "BugFixes", "KnownIssues"]
    for key in required_keys:
        if key not in pr_data:
            raise ValueError(f"Missing required key: {key}")
    return pr_data

def main(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        pr_data = parse_and_validate_json(content)
        print("JSON parsed and validated successfully:", pr_data)
    except Exception as e:
        print(f"Error processing JSON file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update.py <filename>")
        sys.exit(1)
    main(sys.argv[1])
