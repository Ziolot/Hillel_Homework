glory = 100
velocity = int(input('Speed: '))
time = int(input('Time: '))
if velocity > 0:
    distance = time * velocity
    distance_left = glory - distance
    print('Km left until finish:',abs(distance_left))
elif velocity < 0:
    distance = time * velocity * -1
    distance_left = glory + distance
    print ('Km left until finish:',abs(distance_left), '. Turn around!')
else:
    print('Lazy potato')