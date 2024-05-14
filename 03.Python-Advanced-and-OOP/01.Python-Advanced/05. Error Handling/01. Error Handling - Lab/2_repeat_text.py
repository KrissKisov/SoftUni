text = input()

try:
    times = int(input())
    print(text * times)
except ValueError:
    print("Variable times must be an integer")

# example_folder input and output
# Ex.1
# input -> Hello
# input -> Bye
# output -> Variable times must be an integer
# Ex.2
# input -> Hello
# input -> 2
# output -> HelloHello
