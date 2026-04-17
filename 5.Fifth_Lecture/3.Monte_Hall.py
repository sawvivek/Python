import random
doors=[0]*3
goatdoor=[0]*2

swap=0
dont_swap=0

x=random.randint(0,2)
doors[x]="BMW"
for i in range(3):
    if(i==x):
        continue
    else:
        doors[i]="Goat"
        goatdoor.append(i)
        
choice =int(input("Enter your choice of door: "))
door_open=random.choice(goatdoor)
while(door_open==choice):
    door_open=random.choice(goatdoor)
ch=input("Do you want to swap? (y/n): ")
if(ch=='y'):
    if(doors[choice]=="Goat"):
        print("You win a BMW")
        swap+=1
    else:
        print("You lose!")
else:
    if(doors[choice]=="BMW"):
        print("You win a BMW")
        dont_swap+=1
    else:
        print("You lose!")

print("Swap wins: ",swap)
print("Don't swap wins: ",dont_swap)