import json
import re

def convert_to_json(input_data):
    print("first data")
    # Step 1: Add quotes around keys (words followed by a colon)
    formatted_data = re.sub(r'(?P<key>\b\w+\b)(\s*:\s*)', r'"\g<key>"\2', input_data)

    # Step 2: Add quotes around string values
    formatted_data = re.sub(r'(:\s*)([A-Za-z][\w\s]*)([,\n}])', r'\1"\2"\3', formatted_data)

    # Step 3: Ensure all list items and key-value pairs have commas where needed
    formatted_data = re.sub(r'(?<=[}\]"\'\d])(\s*)([}\]])', r',\1\2', formatted_data)
    formatted_data = re.sub(r',(\s*[}\]])', r'\1', formatted_data)  # Remove trailing commas

    # Step 4: Correct double quote issues from step 2 corrections
    formatted_data = re.sub(r'"\s*"\s*:', r'":', formatted_data)
    formatted_data = re.sub(r'"\s*"\s*,', r'",', formatted_data)

    # Debugging output
    print(formatted_data)
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
    corrected_content = convert_to_json(content)
    print("here is corrected context", corrected_content)
    data = parse_json(corrected_content)
    print("Processed Data:", data)

if __name__ == "__main__":
    main()
