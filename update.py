import json
import re

def correct_json_like_content(content):
    # Correcting missing quotes around keys
    content = re.sub(r'(\w+)\s*:', r'"\1":', content)
    # Correcting missing quotes around string values
    content = re.sub(r':\s*([^",{}\[\]\d]+)', r': "\1"', content)
    # Ensure the last values before closing brackets have correct commas
    content = re.sub(r'("[^"]+")\s*([}\]])', r'\1,\2', content)
    return content

def parse_json(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        exit(1)

def main():
    with open('pr_body', 'r') as file:
        content = file.read()
    corrected_content = correct_json_like_content(content)
    data = parse_json(corrected_content)
    print("Processed Data:", data)

if __name__ == "__main__":
    main()
