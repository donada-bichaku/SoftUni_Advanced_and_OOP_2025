def draw_triangle(num):
    if num == 0:
        return

    print("*" * num)

    draw_triangle(num-1)

    print("#" * num)

n = int(input())
draw_triangle(n)
