print("an a=")
a = int(input())
print("an b")
b = int(input())
print("an c")
c = int(input())
if a == 0:
    if b == 0:
        if c == 0:
            print(" pt vo so nghiem")
        else:
            print("pt vo nghiem")
    else:
        x = -c / b
        print(" pt co nghiem kep " + str(x))
else:
    detal = b * b - 4 * a * c
    if detal >= 0:
        if detal == 0:
            x = -b / (2 * a)
            print("pt co nghiem kep" + str(x))
        else:
            x1 = (-b - sqrt(detal)) / (2 * a)
            x2 = (-b + sqrt(detal)) / (2 * a)
            print("pt co nghiem")
            print(str(x1) + " va " + str(x2))
    else:
        print("pt vo nghiem")