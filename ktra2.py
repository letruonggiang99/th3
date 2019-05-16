# nhập chuỗi S và in ra từng kí tự của S, mỗi Ký tự trên một dòng
s=input("nhap chuoi").split()
s=list(set(s))
s.sort()
print(s)