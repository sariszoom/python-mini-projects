from tkinter.messagebox import YES


print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game?(yes/no) \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input(' What is CPU stands for? \n ')
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 1
else:
    print('It\'s wrong')
 
answer = input(' What is GPU stands for? \n ')
if answer.lower() == 'graphical processing unit':
    print('that\'s right!')
    score += 1
else:
    print('It\'s wrong')

answer = input(' What is RAM stands for? \n ')
if answer.lower() == 'random access memory':
    print('that\'s right!')
    score += 1
else:
    print('It\'s wrong')

answer = input(' What is ROM stands for? \n ')
if answer.lower() == 'read only memory':
    print('that\'s right!')
    score += 1
else:
    print('It\'s wrong')

answer = input(' Mouse is an input device or output device? \n ')
if answer.lower() == 'input device':
    print('that\'s right!')
    score += 1
else:
    print('It\'s wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")