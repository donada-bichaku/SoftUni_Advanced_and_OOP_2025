# Returning iterator object - Solution 1
# class vowels:
#     def __init__(self, text:  str):
#         self.text = text
#
#     def __iter__(self):
#         return filter(lambda x: x in ("a", "e", "o", "u", "y", "i"), self.text)




# Solution 2 - implementing the iterator protocol
# class vowels:
#     def __init__(self, text: str):
#         self.vowels_list = [c for c in text if c.lower() in ("a", "e", "o", "u", "y", "i")]
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.vowels_list):
#             result = self.vowels_list[self.index]
#             self.index += 1
#             return result
#         raise StopIteration
#
# # Usage
# v = vowels("tektovi raboti")
# for some in v:
#     print(some)



# Solution 3 - using generator which for loop can call next on without having to define our own next in the class
class vowels:
    def __init__(self, text: str):
        self.text = text
        self.index = 0

    def __iter__(self):
        return (c for c in self.text if c.lower() in ("a", "e", "o", "u", "y", "i"))


# # Usage
# v = vowels("tektovi raboti")
# for some in v:
#     print(some)

