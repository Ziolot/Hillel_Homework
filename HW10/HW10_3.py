def change(list, move):
    if move < 0:
        move = abs(move)
        for n in range(move):
            list.append(list.pop(0))
        else:
            for n in range(move):
                list.insert(0, list.pop())


my_list = [4, 8, 15, 16, 23, 42]
print(my_list)

change(my_list, 3)
print(my_list)

change(my_list, -2)
print(my_list)
