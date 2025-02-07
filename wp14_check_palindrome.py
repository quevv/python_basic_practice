import string

def is_palindrome(value):
    filtered = ''.join(c.lower() for c in str(value) if c in string.ascii_letters + string.digits)
    return filtered == filtered[::-1]

print(is_palindrome('7878787'))
print(is_palindrome('A man, a plan, a canal, Panama!')) 
print(is_palindrome('Was it a car or a cat I saw?')) 
print(is_palindrome("No 'x' in Nixon")) 