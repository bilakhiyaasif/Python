"""
find simple interest of deposit
I=PRN/100
Developer:Bilakhiya Asif
"""
print("--------------------------------")
p=int(input("Enter Price:\t\t"))
r=int(input("Enter Rate:\t\t"))
n=int(input("Enter Num of year:\t"))
print("--------------------------------")

i=(p*r*n)//100;
print("--------------------------------")
print("Price:\t\t\t"+str(p))
print("Rate:\t\t\t"+str(r))
print("Num of year:\t\t"+str(n))
print("Simple Interest:\t"+str(i))
print("--------------------------------")

