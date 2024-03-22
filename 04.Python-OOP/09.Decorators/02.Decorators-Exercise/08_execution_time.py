from time import time


def exec_time(function):
    def wrapper(*args, **kwargs):
        begin = time()
        function(*args, **kwargs)
        finish = time()
        result = finish - begin

        return result

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10_000_000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(10_000_000)]))


@exec_time
def loop():
    count = 0
    for i in range(1, 9_999_999):
        count += 1


print(loop())
