# Display numbers divisible by 5 from a list

def print_divisible_by_5(nums):
    print("Given list is:", nums)
    print("Number/s that is/are divisible by 5:")
    for num in nums:
        if num % 5 == 0:
            print(num)

numbers = [10, 20, 33, 46, 55]
print_divisible_by_5(numbers)
