
def capitalize_words(s):
    return None if not s else ' '.join(s.split()).title()

print(capitalize_words('không  có gì    quý hơn  độc lập      tự do'))
print(capitalize_words('    '))