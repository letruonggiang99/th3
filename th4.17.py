for num in range(1,1000000):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break
