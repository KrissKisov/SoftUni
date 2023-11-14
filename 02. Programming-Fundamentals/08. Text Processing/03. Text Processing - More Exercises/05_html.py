title = input()
content = input()
comments = []
command = input()
while command != "end of comments":
    comments.append(command)

    command = input()

print(f"<h1>\n"
      f"    {title}\n"
      f"</h1>")
print(f"<article>\n"
      f"    {content}\n"
      f"</article>")
for comment in comments:
    print(f"<div>\n"
          f"    {comment}\n"
          f"</div>")
