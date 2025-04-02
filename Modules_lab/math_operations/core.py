
sign_mapper = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a/b if b !=0 else None,
    "^": lambda a,b: a**b,
}

def execute_math(exp):
    num1, sign, num2 = exp.split()
    return sign_mapper[sign](int(num1), int(num2))


