"""
Operators
Developer:Bilakhiya Asif
"""

a,b,c=10,5,2
print("--------------------------------")
print("Arithmetic Operators")
print("--------------------------------")
print("a=\t\t",a)
print("b=\t\t",b)
print("c=\t\t",c)
print("sum=",(a+b))
print("Difference=",(a-b))
print("Product=",(a*b))
print("Quotient=",(a/b))
print("Remainder=",(a%b))
print("Exponent=",(b**2))
print("Floor Division=",(b//c))
print("--------------------------------")

a,b,c=10,5,2
print("Comparison Operators")
print("--------------------------------")
print("a=\t\t",a)
print("b=\t\t",b)
print("c=\t\t",c)
print("a==b is\t",a==b)
print("a!=b is\t",a!=b)
print("a>b is\t",a>b)
print("a<b is\t",a<b)
print("a>=b is\t",a>=b)
print("a<=b is\t",a<=b)
print("--------------------------------")

a,b,c=10,5,2
print("Assignment Operators")
print("--------------------------------")
print("a=\t\t",a)
print("b=\t\t",b)
print("b=\t\t",c)
a+=2
print("a+=2\t=\t",a)
a-=2
print("a-=2\t=\t",a)
a*=b
print("a*=b\t=\t",a)
a/=b
print("a/=b\t=\t",a)
b%=c
print("b%=c\t=\t",b)
b**=c
print("b**=c\t=\t",b)
b//=c
print("b//=c\t=\t",b)
print("--------------------------------")

print("Bitwise Operators")
print("--------------------------------")
a,b=60,2
print("a\t=\t\t",a)
print("b\t=\t\t",b)
print("a&b\t=\t\t",a&b)
print("a|b\t=\t\t",a|b)
print("a^b\t=\t\t",a^b)
print("~a\t=\t\t",~a)
print("a>>b\t=\t\t",a>>b)
print("a<<b\t=\t\t",a<<b)
print("--------------------------------")

print("Logical Operators")
print("--------------------------------")
a,b,c,d=10,5,2,1
print("a\t=\t\t",a)
print("b\t=\t\t",b)
print("c\t=\t\t",c)
print("d\t=\t\t",d)
print("(a>b)and(c>d)\t=\t",(a>b)and(c>d))
print("(a>b)or(d>c)\t=\t",(a>b)or(d>c))
print("not(a>b)\t=\t",not(a>b))
print("--------------------------------")

print("Membership Operators")
print("--------------------------------")
s='abcde'
print("s\t\t=\t",s)
print("'a' in s\t=\t",'a' in s)
print("'f' in s\t=\t",'f' in s)
print("'f' not in s\t=\t",'f' not in s)
print("--------------------------------")

print("Identity Operators")
print("--------------------------------")
a,b,c=10,10,5
print("a\t\t=\t",a)
print("b\t\t=\t",b)
print("c\t\t=\t",c)
print("a is b\t\t=\t",a is b)
print("a is c\t\t=\t",a is c)
print("a is not b\t=\t",a is not b)
print("--------------------------------")
