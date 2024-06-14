a = input("Input: ")
i = 0
while i < len(a):
    if a[i] in "aeiouAEIOU":
        a = a[:i] + a[i+1:]
    i += 1
print("Output:", a)
