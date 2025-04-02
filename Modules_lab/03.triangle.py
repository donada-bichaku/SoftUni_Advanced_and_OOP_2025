def triangle_print(n):
    for i in range(1, n * 2):
        if i <= n:
            print(*range(1, i+1))
        else:
            stop_range = n - i % n
            print(*range(1, stop_range + 1))


triangle_print(3)

print(*range(3, 0, -1))
