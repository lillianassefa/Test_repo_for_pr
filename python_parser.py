import json
string = """
{
    Date: 2024-05-27,
    Category: Feature,
    Title: New Authentication Feature,
    Preview: This release includes a new authentication feature that improves security.,
    BusinessValues: [
        {
            Item1: Increases security by using multi-factor authentication.
        },
        {
            Item2: Enhances user experience with faster login times.
        },
        {
            Item3: Reduces the risk of unauthorized access.
        }
    ],
    Highlights: [
        {
            Highlight1: Multi-factor authentication implemented.
        },
        {
            Highlight2: Improved login times.
        },
        {
            Highlight3: New security protocols in place.
        }
    ],
    Updates: {
        Task Automation: [
            {
                name: New Automation Feature,
                description: Automates user login process with added security.
            }
        ],
        Workflow Customization: [
            {
                name: New Customization Option,
                description: Allows custom security settings per user.
            }
        ]
    },
    Deprecations: {
        Deprecations: [
            {
                Feature: Old Authentication Method,
                Alternative: Use the new multi-factor authentication.
            }
        ]
    },
    BugFixes: {
        Bug Fixes: [
            {
                Description: Fixed slow login issue.,
                Impact: medium
            },
            {
                Description: Resolved intermittent logout problem.,
                Impact: low
            }
        ]
    },
    KnownIssues: [
        {
            Issue1: Intermittent login failures under high load.
        },
        {
            Issue2: Occasional delays in multi-factor authentication.
        }
    ]
} """


def insert_quotes(s, start=0, skip=False):
    i = start
    n = len(s)
    while i < n:
        while i < n and (s[i] == ' ' or s[i] == '\n'):
            i += 1

        if s[i] == "{" or (s[i] != "["):

            if skip:
                i = i-1
            i += 1
            while i < n and (s[i] == ' ' or s[i] == '\n'):
                i += 1
            if i < n:
                s = s[:i] + '"' + s[i:]
                i += 1
            
            if skip:
                i = i+1
            while i < n and s[i] != ':':
                i += 1
            if i < n:
                j = i - 1
                while j > start and (s[j] == ' ' or s[j] == '\n' or s[j] == ',' or s[j] == ']', s[j] == "}"):
                    j -= 1
                s = s[:j+1] + '"' + s[j+1:]
                i += 1
            
            i += 1
            while i < n and (s[i] == ' ' or s[i] == '\n'):
                i += 1
            if i < n and (s[i] == '{' or s[i] == '['):
                s, i = insert_quotes(s, i)
            else:
                s = s[:i] + '"' + s[i:]
                i += 1
            
            while i < n and s[i] not in [',', '}']:
                i += 1
            if i < n and s[i-1] not in [']', '}']:
                j = i - 1
                while j > start and (s[j] == ' ' or s[j] == '\n'):
                    j -= 1
                s = s[:j+1] + '"' + s[j+1:]
                i += 1

        # Recursive call after a comma
        if i < n and s[i] == ',':
            i += 1
            while i < n and (s[i] == ' ' or s[i] == '\n'):
                i += 1
            
                
            if i < n:
                s, i = insert_quotes(s, i-1, True)

        i += 1

    return s, i



if __name__ == "__main__":
    print(string, "..................................")
    value, i = insert_quotes(string)

    print(value, "...............................")