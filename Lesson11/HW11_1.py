win = int(input('Team won -'))
draw = int(input('Team draw - '))
loss = int(input('Team loss - '))


def points(win, draw, loss):
    return (win * 3) + (draw * 1) + (loss * 0)


print('Total score: ' + str(points(win, draw, loss)))
