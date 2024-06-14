a = list(input("camelCase: "))
for i in range(len(a)):
    if a[i].isupper():
        a[i] = a[i].lower()
        a = str(a)
        a = a[:i] + "_" + a[i:]
print(a)