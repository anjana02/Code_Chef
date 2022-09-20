# Write a python program to demonstrate the concept of variable length argument to calculate the sum and product of first 10 numbers


def sum_product(numbers):
    sum = 0
    product = 1
    for number in numbers:
        sum += number
        product *= number
    return sum, product


print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))