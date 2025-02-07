
def filter_integers_greater_than(l, n):
    #return a list has i in l list if i > n
    return [i for i in l if i > n]

l = [0, 3, 5, -2, 9, 8]

print(filter_integers_greater_than(l, 4))