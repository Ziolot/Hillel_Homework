number = float(input('Type in number:'))
deci= number % 1
print(round(deci,3))
print(int(number*10) % 10)
 #
  
  
  # OR
number = float(input('Type in number:'))
print(int(str(number).split('.')[1]))
print(int(number*10) % 10)
