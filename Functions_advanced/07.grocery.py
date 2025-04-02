# def grocery_store(**kwargs):
#     return "\n".join(f"{el[0]}: {el[1]}" for el in
#                      sorted(kwargs.items(), key=lambda kvp: (-(kvp[1]), -len(kvp[0]), kvp[0])))

# Solution 2
def grocery_store(**kwargs):
    products = sorted(kwargs.items(), key=lambda kvp: (-(kvp[1]), -len(kvp[0]), kvp[0]))
    return "\n".join(f"{p}: {q}" for p, q in products)



print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

