
def string_to_int(s):
    if not isinstance(s, str):
        raise TypeError("Not a string")
    if not s.isdigit():
        raise ValueError("Not a positive integer string expression")

    return int(s)


print(string_to_int("17866"))