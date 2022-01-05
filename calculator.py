print("Calculator")
while True:
    print("Choose Operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    while True:
     x=int(input("Put the number of the operation:"))
     if x==1 or x==2 or x==3 or x==4 :
         break
    print("Give tow numbers:")
    a=float(input())
    if x!=4:
        b=float(input())
    while x==4:
        b=float(input())
        if b!=0:
            break
        else:
            print("You can't divide with 0 give again a number:")
    if x==1:
        z=a+b
    elif x==2:
        z=a-b
    elif x==3:
        z=a*b
    else:
        z=a/b
    print(z)
    print("Would you like to do it again?(y/n)")
    while True:
        ap=str(input("y or n:"))
        if ap=="y" or ap=="n":

            break
    if ap=="n":
        break
input()

