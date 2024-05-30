import json
import re
import sys

def correct_and_parse_json_like_content(content):
    corrected_content = re.sub(r'(\w+)(\s*:\s*)', r'"\1"\2', content)
    corrected_content = re.sub(r'(:\s*)([^\d\[\{"][\w\s]+)([,\]\}])', r'\1"\2"\3', corrected_content)
    corrected_content = re.sub(r'(:\s*)([^\d\[\{"][\w\s]+)(\s*[\]\}])', r'\1"\2"\3', corrected_content)
    print(corrected_content)
    return corrected_content
def preprocess_data(data):
    # Adding quotes around keys
    data = re.sub(r'(\w+):', r'"\1":', data)
    # Adding quotes around string values
    data = re.sub(r':\s*([\w\s,.]+)', r': "\1"', data)
    return data

def parse_data(data):
    data = preprocess_data(data)
    return json.loads(data)



def validate_json(data):
    required_keys = ["Date", "Category", "Title", "Preview", "BusinessValues", "Highlights", "Updates", "Deprecations", "BugFixes", "KnownIssues"]
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

def process_json_file(content):
    corrected_content = correct_and_parse_json_like_content(content)
    try:
        pr_data = json.loads(corrected_content)
    except json.JSONDecodeError:
        print("Failed to decode JSON")
        sys.exit(1)

    try:
        validate_json(pr_data)
    except ValueError as e:
        print(f"Validation error: {e}")
        sys.exit(1)

    print("JSON parsed and validated successfully.")
    # Additional processing can continue here, similar to your existing print statements...


