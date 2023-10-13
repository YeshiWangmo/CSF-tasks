def find_longest_word(input_string):
    words = input_string.split()
    longest_word = max(words, key=len)
    return longest_word
print(find_longest_word("This is a test string"))
