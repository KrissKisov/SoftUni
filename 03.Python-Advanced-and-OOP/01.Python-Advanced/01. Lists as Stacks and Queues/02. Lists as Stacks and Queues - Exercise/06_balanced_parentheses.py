from collections import deque

parentheses = deque(input())
opening_parentheses = "{[("
closing_parentheses = "}])"
balanced = "()[]{}"
queue = deque()

while parentheses:
    bracket = parentheses.popleft()
    if bracket in opening_parentheses:
        queue.append(bracket)
    elif bracket in closing_parentheses:
        if queue:
            if queue and queue.pop() + bracket in balanced:
                continue
            else:
                print("NO")
                break
        else:
            print("NO")
            break
else:
    print("YES")
