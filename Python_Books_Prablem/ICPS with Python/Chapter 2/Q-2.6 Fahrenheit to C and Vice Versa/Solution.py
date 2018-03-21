"""
Fahrenheit to Celsius
t=hb/2
Developer:Bilakhiya Asif
"""
def f_t_c():
	print("--------------------------------")
	f=float(input("Enter Temperature in Fahrenheit: "))
	c=(f-32.0)
	c=c*(0.5556)
	print("Celsius: "+str(c)+"C")
	print("--------------------------------")
	
def c_t_f():
	print("--------------------------------")
	c=float(input("Enter Temperature in Celsius: "))
	f=c*(1.8)
	f=f+32.0
	print("Fahrenheit: "+str(f)+"F")
	print("--------------------------------")
	
print("--------------------------------")
print("1.Fahrenheit to Celsius:\t")
print("2.Celsius to Fahrenheit:\t")
ch=int((input("Enter Your Chioce:\t")))
print("--------------------------------")

if ch==1:
	f_t_c()
elif ch==2:
	c_t_f()
else:
	print("Invalid Input")

