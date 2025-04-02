from datetime import datetime, timezone

class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z%z")
        with open("results.txt", "a") as log:
            log.writelines(f"{current_time} - Function '{self.func.__name__}' was called. Result: {result}\n")

        return result


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(46, 2)
mult(5, 10)
