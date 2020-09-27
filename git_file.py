x = int(input("Enter a no."))

while True:
    y = str(x)
    z = y[::-1]
    a = 0
    b = len(y) - 1
    for i in range(b):
        if z[i] == y[i]:
            a += 1
    if a == b:
        print(y)
        break
    else:
        x += 1