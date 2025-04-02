def type_check(argument):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, argument):
                return "Bad Type"
            return func(arg)
        return wrapper
    return decorator


# @type_check(str)
# def first_letter(word):
#     return word[0]
#
# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))

