# Solution 1
# def func_executor(*args):
#     result = []
#     for arg in args:
#         result.append((arg[0].__name__, arg[0](*arg[1])))
#     return "\n".join(f"{pair[0]} - {pair[1]}" for pair in result)

# Solution 2
# def func_executor(*args):
#     result = []
#     for func, arg in args:
#         result.append(f"{func.__name__}, {func(*arg)}")
#     return "\n".join(result)


# Solution 3
def func_executor(*args):
    return "\n".join(f"{func.__name__}, {func(*arg)}" for func, arg in args)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
