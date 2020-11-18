def triangle():
    a = float(input("Base:"))
    h = float(input("High: "))
    print("Area: %.2f" % (0.5 * a * h))

def square():
    c = float(input("Side"))
    print("Area: %.2f" % (c * c))

figure = input("3-triangle, 4-square: ")
if figure == '3':
  triangle()
elif figure == '4':
  square()
else:
  print("Wrong number")