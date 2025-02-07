
def uppercase_lowercase_words(s):
    words = s.split()
    return ' '.join(
        word.upper() 
        if i % 2 == 0 
        else word.lower() 
        for i, word in enumerate(words))


print(uppercase_lowercase_words('one two three four five'))
print(uppercase_lowercase_words('SIX SEVEN EIGHT NINE TEN'))
print(uppercase_lowercase_words('1 one two 2 3 three four 4 five six'))