
def char_to_int(c):
    if not isinstance(c, str):
        raise TypeError("Not a string")
    if len(c) != 1 or not ('0' <= c <= '9'):
        raise ValueError("Not a single digit")
    
    return ord(c) - ord('0')

print(char_to_int('2'))