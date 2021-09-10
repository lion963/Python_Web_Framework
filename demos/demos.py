# def factorial(num):
#     if num < 2:
#         return 1
#     return num * factorial(num - 1)
#
#
# print(factorial(0))

# Perfect Number
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors,
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
# Equivalently, a perfect number is a number that is half the sum of all its positive divisors (including itself).
# Write a method that prints the first 4 perfect numbers.

def find_devisors(num):
    devisors = []
    for i in range(1, num+1):
        if num % i == 0:
            devisors.append(i)
    return devisors


def check_perfect(devisors, num):
    if num == sum(devisors) - num:
        return True
    return False


def perfect_nums():
    perfect_num = []
    num = 1
    while len(perfect_num) < 4:
        devisors = find_devisors(num)
        is_perfect = check_perfect(devisors, num)
        if is_perfect:
            perfect_num.append(num)
        num += 1
    return perfect_num

print(perfect_nums())
# devisors = find_devisors(6)
# print(check_perfect(devisors, 6))

