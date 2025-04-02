def negative_positive(*args):
    sum_pos = sum(num for num in args if num > 0)
    sum_neg = sum(num for num in args if num < 0)

    print(sum_neg)
    print(sum_pos)
    print("The positives are stronger than the negatives") if sum_pos > abs(sum_neg) \
        else print("The negatives are stronger than the positives")


numbers = [int(number) for number in input().split()]
negative_positive(*numbers)



