odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(el) for el in input())


    # {even_set.add(sum(ord(el))//i) if (sum(ord(el))//i)%2==0 else even_set.add(sum(ord(el))//i) for el in input()}
    # print(even_set)
    # print(odd_set)
