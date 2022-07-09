from typing import List

#
# def fib(num: int) -> List[int]:
#     numbers = []
#     current, nxt = 0, 1
#     while len(numbers) < num:
#         current, nxt = nxt, current + nxt
#         numbers.append(current)
#
#     return numbers


def fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


result = fib()
# result = []
for n in result:
    print(n, end=', ')
    # if n > 10000:
    #     break

print()
print("Done")
