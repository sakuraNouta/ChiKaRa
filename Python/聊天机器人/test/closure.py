def count():
    a = 1
    b = 1
    def sum():
        c = 1
        return a + c
    return sum

sum = count()
print(sum())
print(count()())
