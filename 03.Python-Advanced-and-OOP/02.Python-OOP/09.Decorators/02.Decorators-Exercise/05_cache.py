def cache(func):

    def wrapper(*args):
        for arg in args:
            if not wrapper.log.get(arg):
                wrapper.log[arg] = func(arg)

            return wrapper.log[arg]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(3)
# print(fibonacci.log)

fibonacci(10)
print(fibonacci.log)
