import random
def rock_paper_scissor(nums1,nums2,bits1,bits2):
    p1=int(nums1[bits1])%3
    p2=int(nums2[bits2])%3
    if(player_one[p1]==player_two[p2]):
        return "It's a tie!"
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        return "Player 1 wins!"
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        return "Player 1 wins!"
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
    
player_one={0:"Rock",1:"Paper",2:"Scissor"}
player_two={0:"Rock",1:"Paper",2:"Scissor"}

while(1):
    nums1=input("Player 1, enter your choice (0-Rock, 1-Paper, 2-Scissor): ")
    nums2=input("Player 2, enter your choice (0-Rock, 1-Paper, 2-Scissor): ")
    bits1=int(input("Player 1, enter the secret bit position (0-2): "))
    bits2=int(input("Player 2, enter the secret bit position (0-2): "))
    result = rock_paper_scissor(nums1,nums2,bits1,bits2)
    print(result)
    ch = input("Do you want to continue? (y/n): ")
    if(ch=='n'):
        break

