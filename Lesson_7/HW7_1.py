def count_words(function):
    def inner():
        print(function().split())
    return inner
@count_words
def entered_string():
    return input("Please enter a sentence: ")

count_words(entered_string())
