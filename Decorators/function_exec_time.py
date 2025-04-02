import time

def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        wrapper.exec_time = end_time-start_time
        return result # return the result of the function
    wrapper.exec_time = 0 # used to get the result of the execution time calculated in the wrapper
    return wrapper


# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
# print(loop(1, 1000))
# print(loop.exec_time)

