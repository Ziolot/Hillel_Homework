import random

number = random.randint(1, 10)
attempt = 1
while attempt < 4:
    guess = int(input('Type in number from 1 to 10:'))
    attempt = attempt + 1
    if guess != number and attempt != 4:
        print('Try again')
    if guess == number:
        print('You Won!')
        break
else:
    print('You lose')
