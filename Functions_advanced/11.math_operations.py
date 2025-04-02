def math_operations(*numbers, **kwargs):
    keys = list(kwargs.keys())

    for i in range(len(numbers)):
        key = keys[i % 4]

        if key == "a":
            kwargs[key] += numbers[i]
        elif key == "s":
            kwargs[key] -= numbers[i]
        elif key == "d":
            if numbers[i] != 0:
                kwargs[key] /= numbers[i]
        elif key == "m":
            kwargs[key] *= numbers[i]

    kwargs = sorted(kwargs.items(), key=lambda kvp: (-(kvp[1]), kvp[0]))
    return "\n".join(f"{key}: {value:.1f}" for key, value in kwargs)



print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
