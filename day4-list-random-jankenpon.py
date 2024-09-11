import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

signs = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(signs[user])

print("Computer chose:")
index = random.randrange(len(signs))
value = signs[index]
print(value)

if user == index:
    print("It's a draw. Good game, well played.")
elif (user == 0 and index == 1) or (user == 1 and index == 2) or (user == 2 and index == 0):
    print("You lose. Better get lucky next time.")
elif (user == 0 and index == 2) or (user == 1 and index == 0) or (user == 2 and index == 1):
    print("You win! Congratulation mate!")
else:
    print("Monkey D Garp yells, 'GALAXY IMPACTOOO!'. You died.")
