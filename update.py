import json
import sys
import os

def validate_json(data):
    """
    Validate the JSON data.
    This is a placeholder function. You can add custom validation logic here if needed.
    """
    required_keys = ["Date", "Category", "Title", "Preview", "BusinessValues", "Highlights", "Updates", "Deprecations", "BugFixes", "KnownIssues"]
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

def process_json_file(file_path):
    """
    Process the JSON data from the given file path.
    """
    with open(file_path, 'r') as file:
        pr_data = json.load(file)
        validate_json(pr_data)
        print("TEST PASSED")
        
        print("Date:", pr_data["Date"])
        print("Category:", pr_data["Category"])
        print("Title:", pr_data["Title"])
        print("Preview:", pr_data["Preview"])
        
        print("\nBusiness Values:")
        for i, item in enumerate(pr_data["BusinessValues"], start=1):
            print(f"  Item {i}: {item}")
        
        print("\nHighlights:")
        for i, highlight in enumerate(pr_data["Highlights"], start=1):
            print(f"  Highlight {i}: {highlight}")
        
        print("\nUpdates:")
        for category, updates in pr_data["Updates"].items():
            print(f"  {category}:")
            for update in updates:
                print(f"    Name: {update['name']}")
                print(f"    Description: {update['description']}")
        
        print("\nDeprecations:")
        for deprecation in pr_data["Deprecations"]["Deprecations"]:
            print(f"  Feature: {deprecation['Feature']}")
            print(f"  Alternative: {deprecation['Alternative']}")
        
        print("\nBug Fixes:")
        for bug_fix in pr_data["BugFixes"]["Bug Fixes"]:
            print(f"  Description: {bug_fix['Description']}")
            print(f"  Impact: {bug_fix['Impact']}")
        
        print("\nKnown Issues:")
        for i, issue in enumerate(pr_data["KnownIssues"], start=1):
            print(f"  Issue {i}: {issue}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_json_file.py <path_to_json_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist")
        sys.exit(1)
    
    try:
        process_json_file(file_path)
    except ValueError as e:
        print(f"Validation error: {e}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Failed to decode JSON")
        sys.exit(1)
