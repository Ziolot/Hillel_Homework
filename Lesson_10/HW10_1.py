my_list = []

while True:
    The_string_for_text = input('Please, enter some text. To stop the process, please enter empty line. ')
    if The_string_for_text != '':
        my_list.append(The_string_for_text)
    if The_string_for_text == '':
        break

with open('HW10_1.txt', 'w') as w:
    for line in my_list:
        w.write(line + '\n')
