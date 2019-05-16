n=input("nhap chuoi:")
dict ={'h':0,'t':0}
for i in n:
    if i .isupper():
        dict['h']=dict['h']+1
    elif i!=' ':
        dict['t']+=1
        print(dict)