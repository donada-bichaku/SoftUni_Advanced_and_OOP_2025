from math import log

def read_user_input():
    user_input = []
    user_input.append(int(input("Enter the number: ")))

    while True:
        input2 = (input("Enter the base (number or natural): "))
        try:
            num2 = int(input2)
            user_input.append(num2)
            break
        except ValueError:
            if input2 == "natural":
                break
            else:
                print("Please enter a valid base, either a number or write 'natural' for natural log")
                continue

    return user_input


def calculate_result():
    nums = read_user_input()
    if len(nums) == 1:
        return log(nums[0])
    else:
        return log(nums[0], nums[1])


def print_result():
    print(f"{calculate_result():.2f}")


print_result()



