# import matplotlib.pyplot as plt
# import numpy as np

# plt.plot([1,2,3,4],[1,4,9,16]) 
# plt.xlabel('some numbers') 
# plt.ylabel('some numbers')       
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16],'ro') 
# plt.xlabel('some numbers') 
# plt.ylabel('some numbers')       
# plt.show()
# plt.plot([1,2,3,4],[1,4,9,16],'r--') 
# plt.xlabel('some numbers') 
# plt.ylabel('some numbers')       
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16],'bs') 
# plt.xlabel('some numbers') 
# plt.ylabel('some numbers')       
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16],'g^') 
# plt.xlabel('some numbers') 
# plt.ylabel('some numbers')       
# plt.show()


# Permutation

def play():
    p1name = input("Player 1, please enter your name: ")
    p2name = input("Player 2, please enter your name: ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if turn%2==0:
            print(p1name,"Your turn")
            ans=input("What is on my mind? ")
            if ans==picked_word:
                pp1+=1
                print("Your score is ",pp1)
            else:
                print("Better luck next time! I thought of ",picked_word)
            c=input("Press 1 to continue and 0 to quit: ")
            if c=='0':
                thanks(p1name,pp1,p2name,pp2)
                break
        else:
            print(p2name,"Your turn")
            ans=input("What is on my mind? ")
            if ans==picked_word:
                pp2+=1
                print("Your score is ",pp2)
            else:
                print("Better luck next time! I thought of ",picked_word)
            c=input("Press 1 to continue and 0 to quit: ")
            if c=='0':
                thanks(p1name,pp1,p2name,pp2)
                break
        turn+=1
        
def choose():
    import random
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    import random
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thanks(p1name,pp1,p2name,pp2):
    print("Thanks for playing the game!")
    print(p1name,"Your score is ",pp1)
    print(p2name,"Your score is ",pp2)
    
play()
