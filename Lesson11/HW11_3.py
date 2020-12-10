def longest_word (some_list):
    return max(some_list.split(), key=len)


some_list = 'what makes a good man'
print(longest_word(some_list))