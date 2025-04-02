from math import isqrt


def get_primes(numlist):

    for num in numlist:
        if num <= 1:
            continue

        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                break
        else:
            yield num







