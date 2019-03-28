str=input("Enter a String:")
dict = { }
for n in str:
    keys = dict. keys ()
    if n in keys:
        dict [n] += 1
    else:
        dict[n] = 1
    print (dict)


str=input("Enter a String")
dict = { }
for i in str:
    dict[i] = str.count(i)
print (dict)
