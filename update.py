import json

def parse_json(content):
    try:
        result = json.loads((content))
        print("result type", type(result))
        return result

    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        exit(1)

def main():
    print("entered main")
    with open('pr_body.json', 'r') as file:
        content = file.read()
    print("here is the content", content)
    print(type(content), "typeeeeeeee")
    
    data = parse_json(content)
    print("Processed Data:", data, type(data), "final typeeeeeeeee")
    date = data['Date']
    category = data['Category']
    title = data['Title']
    preview = data['Preview']
    business_values = data['BusinessValues']
    highlights = data['Highlights']
    updates = data['Updates']
    deprecations = data['Deprecations']
    bug_fixes = data['BugFixes']
    known_issues = data['KnownIssues']

    print(f"Date: {date}")
    print(f"Category: {category}")
    print(f"Title: {title}")
    print(f"Preview: {preview}")
    print("Business Values:", business_values)
    print("Highlights:", highlights)
    print("Updates:", updates)
    print("Deprecations:", deprecations)
    print("Bug Fixes:", bug_fixes)
    print("Known Issues:", known_issues)

if __name__ == "__main__":
    main()
