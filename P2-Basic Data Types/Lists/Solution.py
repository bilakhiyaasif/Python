def insertdata(string,li):
    pos=int(string[1])
    data=int(string[2])
    li.insert(pos,data)
    return li


def appenddata(string,li):
    data=int(string[1])
    li.append(data)
    return li

def removedata(string,li):
    data=int(string[1])
    return li.remove(data)
    return li

def sortdata(string,li):
    li=li.sort()
    return li

def popdata(string,li):
    return li.pop()



n=int(input())
li=[]
for i in range(n):
    command=input()
    string=command.split()
    if string[0]=="insert":
        li=insertdata(string,li)
    if string[0]=="append":
        li=appenddata(string,li)
    if string[0]=="remove":
        li.remove(int(string[1]))
    if string[0]=="print":
        print(li)
    if string[0]=="sort":
        li.sort()
    if string[0]=="pop":
        li.pop()
    if string[0]=="reverse":
        li.reverse()
