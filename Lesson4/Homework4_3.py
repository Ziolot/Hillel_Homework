number_one = int(input('Number A is : '))
number_two = int(input('Number B is : '))
if number_one < number_two:
    for i in range(number_one, number_two + 1):
     print(i)
else:
    for i in range(number_one, number_two - 1, -1):
            print(i)



