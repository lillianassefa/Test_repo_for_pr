import json
import re


def correct_json_like_content(content):
    print("origninal:", content)
    # Add quotes around keys (preceded by a newline or a comma, followed by a colon)
    content = re.sub(r'(?<=\{|\,)\s*([A-Za-z0-9]+)\s*:', r'"\1":', content)
    
    # Add quotes around string values (if they start with a word character, end with a non-quote followed by a comma or closing bracket)
    content = re.sub(r':\s*([A-Za-z0-9\s]+?[\w])(?=[,\n}])', r': "\1"', content)
    
    # Fix trailing commas (if the next non-space character is a closing bracket or another comma, remove it)
    content = re.sub(r',\s*([\]}])', r'\1', content)
    print("final", content)
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
    corrected_content = correct_json_like_content(content)
    print("here is corrected context", corrected_content)
    data = parse_json(corrected_content)
    print("Processed Data:", data)

if __name__ == "__main__":
    main()
