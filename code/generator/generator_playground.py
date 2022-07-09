
""" CSV READER """
# def csv_reader(file_name):
#     file = open(file_name)
#     result = file.read().split("\n")
#     return result
file_name = "../some_csv.txt"


def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


csv_gen = csv_reader(file_name )

# csv_gen = (row for row in open(file_name))

row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")


"""INFINITE SEQUENCE"""
a = range(5)
print(list(a))


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# for i in infinite_sequence():
#     print(i, end=" ")

gen = infinite_sequence()
next(gen)


"""PALINDROME DETECTOR"""


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


# for i in infinite_sequence():
#     pal = is_palindrome(i)
#     if pal:
#         print(i)

# """GENERATOR EXPRESSIONS"""
# nums_squared_lc = [num**2 for num in range(5)]
# nums_squared_gc = (num**2 for num in range(5))

"""PROFILING GENERATOR PERFORMANCE"""
import sys
nums_squared_lc = [i ** 2 for i in range(10000)]
print(str(sys.getsizeof(nums_squared_lc)) + " bytes")
nums_squared_gc = (i ** 2 for i in range(10000))
print(str(sys.getsizeof(nums_squared_gc)) + " bytes")

import cProfile

cProfile.run('sum([i * 2 for i in range(10000)])')
print("-------")
cProfile.run('sum((i * 2 for i in range(10000)))')
"""Here, you can see that summing across all values in the list 
comprehensiontook about a third of the time as summing across 
the generator. If speed is an issue and memory isn’t, then a list
 comprehension is likely a better tool for the job."""


"""ADVANCED PALINDROME DETECTOR WITH .send() .throw() .close()"""


def advanced_is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1


pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))

