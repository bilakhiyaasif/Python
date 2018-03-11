"""
Exercise 2 (and Solution)

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
	Author:Bilakhiya Asif
"""
n=int(input("Enter Number:"))
if n%2==0:
	print(str(n)+" is Even.")
else:
	print(str(n)+" is odd.")
