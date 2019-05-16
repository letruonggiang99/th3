S = input("Nhap chuoi can kiem tra ---> ")
dict={'Chu':0 ,'So':0}
for i in S:
    if i.isalpha():
        dict['Chu'] += 1
    else:
        dict['So'] +=  1
print(dict)
