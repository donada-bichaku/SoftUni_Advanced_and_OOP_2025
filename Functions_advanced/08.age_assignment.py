def age_assignment(*names, **name_age):
    result = []
    for key, age in name_age.items():
        for name in names:
            if name.startswith(key):
                result.append(f"{name} is {age} years old.")
                break
    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
