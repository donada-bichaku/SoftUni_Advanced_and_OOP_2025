def even_parameters(func):
     def wrapper(*args):
         if not all(isinstance(arg, int) and arg % 2 == 0 for arg in args):
             return "Please use only even numbers!"
         result = func(*args)
         return result
     return wrapper



# @even_parameters
# def add(a, b):
#     return a + b
#
# print(add(2, 4))
# print(add("Peter", 1))
