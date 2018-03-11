"""
Exercise 1 (and Solution)
Character Input
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
	
	Author: Bilakhiya Asif
	
"""
Name=(input("Enter your Name:"))
Age=int(input("Enter Age:"))
print("Your Name: "+Name,end="\n")
print("Your Age: "+str(Age),end="\n")
Age=100-Age
Age=2018+Age
print("You turn 100 on: "+str(Age))
