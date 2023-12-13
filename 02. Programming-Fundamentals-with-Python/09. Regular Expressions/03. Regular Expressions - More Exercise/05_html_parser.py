import re


def title(some_file):
    pattern = r"(?<=<title>)([\w+\s?]*)(?=<\/title>)"
    match = re.findall(pattern, some_file)
    if match:
        match = "".join(match)
        final_match = re.sub(html_tags_skip, "", match)
        return final_match


def content(some_file):
    pattern = r"(?<=<body>).+(?=<\/body>)"
    match = re.findall(pattern, some_file)
    if match:
        match = "".join(match)
        final_match = re.sub(html_tags_skip, "", match)
        return final_match


html_file = input()
html_tags_skip = r"((<[^<]+>)|(\\n))"
print(f"Title: {title(html_file)}")
print(f"Content: {content(html_file)}")
