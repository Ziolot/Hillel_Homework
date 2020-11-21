import time


def count_down(func):
    def seconds():
        for i in range(1, 4):
            print(i)
            time.sleep(1)
        func()
    return seconds()


@count_down
def time_now():
    print(time.strftime('%H:%M'))
