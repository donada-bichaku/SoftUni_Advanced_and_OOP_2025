def create_sequence(num):
    nums = [0, 1]
    [nums.append(nums[-1] + nums[-2]) for _ in range(num-2)]
    return nums


def locate_sequence(num, seq):
    try:
        idx = seq.index(num)
        return f"The {num} is in index {idx}."
    except ValueError:
        return f"The {num} is not in the sequence."

