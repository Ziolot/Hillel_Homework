def isprime(Argument):
    for i in range(0, 1000):
        if Argument % 2 == 0 and Argument != 2:
            return False
        if Argument == 0 or Argument == 1:
            return False
        return True


Argument = int(input('Enter a number from 0 to 1000: '))
print(isprime(Argument))
