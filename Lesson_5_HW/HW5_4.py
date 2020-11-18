import random

random_list = [random.randint(1, 100) for i in range(100)]
print(random_list)
A_list = []
for i in random_list:
    if i % 2 ==0:
        A_list.append(i)
    else:
        A_list.append(0)

print(A_list)
print('Amount of odd numbers are: ', A_list.count(0))