word_for_check = input('Is it palindrome: ')


def palindrome_check(a):
    word = [str(ch) for ch in a]
    check_reverse = word[::-1]
    if word == check_reverse:
        print('Yes, it is!')
    else:
        print('No, it isn`t')
    return a


palindrome_check(word_for_check)