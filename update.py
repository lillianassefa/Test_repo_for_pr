import json
import re


def parse_json(content):
    try:
        temp = json.dumps(content)
        print("temp type", type(temp))
        result = dict(json.loads(str(temp)))
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

if __name__ == "__main__":
    main()
