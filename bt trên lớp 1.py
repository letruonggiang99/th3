while True:
  try:
    a=int(input("nhap a:"))
    b=int(input("nhap b:"))
    kq=a/b
  except:
    print("loi, nhap lai")
  else:
      break
print("ket qua la:",kq)
