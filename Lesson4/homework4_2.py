import math

numbers = []
even_num = 0
odd_num = 0
max_number = 0
max_numbertwo=0
second_one=0
i = 0

while (x := int(input("Add number but not zero: "))) != 0:
    numbers.append(x)
    if x > max_number:
        max_number = x
        index= i
        i += 1
    elif x == max_number:
        max_numbertwo += 1
    if x == 0:
        break
    elif x % 2 == 0:
        even_num += 1
    elif x % 2 != 0:
        odd_num += 1


def my_mean(numbers):
    return sum(numbers) / len(numbers)

second_one= sorted(numbers)
print(list(numbers), len(numbers), sum(numbers), math.prod(numbers) //
      my_mean(numbers), even_num, odd_num, max_number, i, second_one[-2], max_numbertwo)
