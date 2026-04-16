# import random
# movies=["anand","drishyam","nayakan","sarkar","psycho","vikram vedha","kaithi","thani oruvan","vikram","master","gol maal","blank friday","dangal","taare zameen par"]

# def create_question(movie):
#     n=len(movie)
#     letters=list(movie)
#     temp=[]
#     for i in range(n):
#         if letters[i]==" ":
#             temp.append(" ")
#         else:
#             temp.append("*")
#     qn="".join(str(x) for x in temp)
#     return qn

# def is_present(letter,movie):
#     c=movie.count(letter)
#     if c==0:
#         return False
#     else:
#         return True

# def unlock(qn,movie,letter,ch):
#     ref=list(movie)
#     qn_list=list(qn)
#     temp=[]
#     n=len(movie)
#     for i in range(n):
#         if ref[i]==" " or ref[i]==letter:
#             temp.append(ref[i])
#         else:
#             if qn_list[i]=="*":
#                 temp.append("*")
#             else:
#                 temp.append(ref[i])
#     qn_new="".join(str(x) for x in temp)
#     return qn_new  
    
# def play():
#     p1name=input("Player 1, Enter your name: ")
#     p2name=input("Player 2, Enter your name: ")
#     pp1=0
#     pp2=0
#     turn=0
#     willing=True    
#     while(willing):
#         if turn%2==0:
#             print(f"{p1name}'s turn")
#             picked_movie=random.choice(movies)
#             qn=create_question(picked_movie)
#             print(qn)
#             modified_qn=qn
#             not_said=True
#             while(not_said):
#                 letter=input("Your answer: ")
#                 if (is_present(letter,picked_movie)):
#                     modified_qn=unlock(modified_qn,letter,picked_movie)
#                     print(modified_qn)
#                     d=input("Press 1 to guess the movie name or 0 to continue: ")
#                     if d=="1":
#                         ans=input("Your answer: ")
#                         if ans.lower()==picked_movie:
#                             print("Correct Answer")
#                             pp1=pp1+1
#                             not_said=False
#                             print(f"{p1name} has {pp1} points and {p2name} has {pp2} points")
#                         else:
#                             print("Wrong Answer, Try Again")
#                 else:
#                     print("Wrong Answer, Try Again")
#             c=input("Press 1 to continue playing or 0 to stop: ")
#             if c=="0":
#                 print(f"{p1name} has {pp1} points and {p2name} has {pp2} points")
#                 print("Thanks for playing!")
#                 willing=False
#         else:
#             print(f"{p2name}'s turn")
#             picked_movie=random.choice(movies)
#             qn=create_question(picked_movie)
#             print(qn)
#             modified_qn=qn
#             not_said=True
#             while(not_said):
#                 letter=input("Your answer: ")
#                 if (is_present(letter,picked_movie)):
#                     modified_qn=unlock(modified_qn,letter,picked_movie)
#                     print(modified_qn)
#                     d=input("Press 1 to guess the movie name or 0 to continue: ")
#                     if d=="1":
#                         ans=input("Your answer: ")
#                         if ans.lower()==picked_movie:
#                             print("Correct Answer")
#                             pp2=pp2+1
#                             not_said=False
#                             print(f"{p1name} has {pp1} points and {p2name} has {pp2} points")
#                         else:
#                             print("Wrong Answer, Try Again")
#                 else:
#                     print("Wrong Answer, Try Again")
#             c=input("Press 1 to continue playing or 0 to stop: ")
#             if c=="0":
#                 print(f"{p1name} has {pp1} points and {p2name} has {pp2} points")
#                 print("Thanks for playing!")
#                 willing=False
                
#         turn=turn+1
            
# play()

import random

# List of movies as shown in the video
movies = ['anand', 'drishyam', 'nayakan', 'anbe sivam', 'gol maal', 'vikram vedha', 'black friday', 'dangal', 'manichithrathazhu', 'taare zameen par']

def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn

def is_present(letter, movie):
    c = movie.count(letter)
    if c == 0:
        return False
    else:
        return True

def unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i] == ' ' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new = "".join(str(x) for x in temp)
    return qn_new

def play():
    p1name = input('Player 1: Please enter your name: ')
    p2name = input('Player 2: Please enter your name: ')
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    
    while willing:
        if turn % 2 == 0:
            # Player 1's turn
            current_player = p1name
        else:
            # Player 2's turn
            current_player = p2name
            
        print(current_player, 'Your turn')
        picked_movie = random.choice(movies)
        qn = create_question(picked_movie)
        print(qn)
        
        modified_qn = qn
        not_said = True
        
        while not_said:
            letter = input('Your letter: ')
            if is_present(letter, picked_movie):
                modified_qn = unlock(modified_qn, picked_movie, letter)
                print(modified_qn)
                
                decision = input('Press 1 to guess the movie or 2 to unlock another letter: ')
                if decision == '1':
                    ans = input('Your answer: ')
                    if ans == picked_movie:
                        if turn % 2 == 0:
                            pp1 += 1
                        else:
                            pp2 += 1
                        print('Correct!')
                        not_said = False
                    else:
                        print('Wrong answer! Try again.')
            else:
                print(letter, 'not found')
        
        print(f"Points: {p1name}: {pp1}, {p2name}: {pp2}")
        
        c = input('Press 1 to continue or 0 to quit: ')
        if c == '0':
            willing = False
            print(f"Final Score -> {p1name}: {pp1}, {p2name}: {pp2}")
            print('Thanks for playing!')
        else:
            turn += 1

# Start the game
play()