import json
import re

file_path = "updates.json" 
def parse_json(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        exit(1)

def main():
    print("entered main")
    with open('updates.json', 'r') as file:
        content = file.read()
    print("here is the content", content)
   

    data = parse_json(content)
    print("Processed Data:", data)

if __name__ == "__main__":
    main()
