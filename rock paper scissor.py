print("  ROCK PAPER SCISSOR")
print("0 for ROCK\n1 for PAPER\n2 for SCISSOR")
v=int(input("Choose rock paper or scissor"))
import random
s=int(random.randint(0,2))
print(s)
if(v>2):
    print("enter valid number")
if(v==s):
    print("DRAW\nYour choice and computer choice are same")
elif(v==0 and s==1):
    print(f"your choice ROCK\ncomputer choice is PAPER")
    print("computer wins")
elif(v==0 and s==2):
    print(f"your choice ROCK\ncomputer choice is SCISSOR")
    print("YOU wins")
elif(v==1 and s==0):
    print(f"your choice PAPER\ncomputer choice is ROCK")
    print("YOU wins")
elif(v==1 and s==2):
    print(f"your choice PAPER\ncomputer choice is SCISSOR")
    print("computer wins")
elif(v==2 and s==0):
    print(f"your choice SCISSOR\ncomputer choice is ROCK")
    print("computer wins")
elif(v==2 and s==1):
    print(f"your choice SCISSOR\ncomputer choice is PAPER")
    print("YOU wins")