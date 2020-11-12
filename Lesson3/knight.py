x = int(input('Type in number of cell vertically: '))
y = int(input('Type in number of cell horizontally: '))
x2 = int(input("Type in where you want to move the knight vertically: "))
y2 = int(input('Type in where you want to move the knight horizontally: '))
dx = abs(x - x2)
dy = abs(y - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('You can do it')
else:
    print("You cannot do it")
