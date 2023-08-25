print("            PIZZA ORDER PROGRAM")
o=input("what type of pizza do you want , enter s or m or l\n1.Small pizza = 100  s or S  \n2.Medium pizza = 200 m or M \n3.Large pizza = 300 l or L   ")
bill=0
if o==  's' or o=='S':
    print("small pizza")
    bill=bill+100
    p=input("do you want extra pepparoni y or n")
    if(p=='y' or p=='Y'):
        bill=bill+20
        print(f"bill={bill}")
    else:
        print(f"bill={bill}")
elif(o=='m' or o=="M"):
    print("medium pizza")
    bill = bill+200
    p=input("do you want pepparoni y or n")
    if (p == 'y' or p == 'Y'):
        bill = bill + 30
        print(f"bill={bill}")
    else:
        print(f"bill={bill}")
elif(o=='l' or o== 'L'):
    print("large pizza")
    bill=bill+300
    p = input("do you want pepparoni y or n")
    if (p == 'y' or p == 'Y'):
        bill = bill + 30
        print(f"bill={bill}")
    else:
        print(f"bill={bill}")
if(o==  's' or o=='S' or o== "m" or o=='M' or o=='l' or o== 'L'):
    b=input("do you want extra cheese y or n")
    if(b=='y' or b=='Y'):
        bill=bill+30
print(f"TOTAL BILL= {bill}")
