import random
import getpass
#can be used as a Rock/Paper?Scissors game
# def game(comp, b):   #for computer vs player
#     if comp==b:
#         return None
#     elif comp=='s':
#         if b=='w':
#             return False
#         elif b=='g':
#             return True
#     elif comp=='w':
#         if b=='g':
#             return False
#         elif b=='s':
#             return True
#     elif comp=='g':
#         if b=='s':
#             return False
#         elif b=='w':
#             return True



def game(a, b):
    if a==b:
        return None     #for declaring a tie
    elif a=='s':
        if b=='w':
            return False
        elif b=='g':
            return True
    elif a=='w':
        if b=='g':
            return False
        elif b=='s':
            return True
    elif a=='g':
        if b=='s':
            return False
        elif b=='w':
            return True

# print("Comp Turn: Snake(s), Water(w) or Gun(g)")   #for computer vs player
# randNO=random.randint(1,3)
# print("Computer decided it's move!")
# if randNO==1:
#     comp='s'
# elif randNO==2:
#     comp='w'
# elif randNO==3:
#     comp='g'

a=getpass.getpass(prompt="Player 1 Turn: Snake(s), Water(w) or Gun(g): ")
b=input("Player's Turn: Snake(s), Water(w) or Gun(g): ")



c=game(a, b)
print(f"Comp chose {a}")
print(f"You chose {b}")
if c==None:
    print("the game is a tie!")
elif c:
    print("You win! Player 1 lost")
else:
    print("You lose! Player 1 won")

# a=game(comp, b)        #for computer vs player
# print(f"Comp chose {comp}")
# print(f"You chose {b}")
# if a==None:
#     print("the game is a tie!")
# elif a:
#     print("You win!")
# else:
#     print("You lose!")