import json
import re

import re
import json

def correct_json_formatting(content):
    print("Entered first function with original:", content)
    # Escape unescaped line breaks within strings
    content = re.sub(r'(?<=[^\\])\n', '\\\\n', content)

    # Ensure all strings are correctly closed
    content = re.sub(r'([^\\])"', r'\1\\"', content)
    content = re.sub(r'\\\\"', r'\\"', content)  # Correct double escaping caused by the line above

    # Correct missing quotes at the end of values
    content = re.sub(r'([^"])\s*\n\s*"', r'\1",\n"', content)

    # Attempt to fix any remaining string termination issues
    content = re.sub(r'([^"])\s*,\s*\n\s*}', r'\1"\n}', content)
    content = re.sub(r'([^"])\s*\n\s*}', r'\1"\n}', content)
    print("Final content,", content)
    return content

def parse_json(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        exit(1)

def main():
    print("entered main")
    with open('pr_body', 'r') as file:
        content = file.read()
    print("here is the content", content)
    corrected_content = correct_json_formatting(content)
    print("here is corrected context", corrected_content)
    data = parse_json(corrected_content)
    print("Processed Data:", data)

if __name__ == "__main__":
    main()
