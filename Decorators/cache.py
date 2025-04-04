def cache(func):
    log = {}

    def wrapper(num):
        if num in wrapper.log:
            return wrapper.log[num]
        result = func(num)
        log[num] = result
        return result

    wrapper.log = log
    return wrapper


# @cache
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# fibonacci(3)
# print(fibonacci.log)
