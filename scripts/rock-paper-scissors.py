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

def playGame():
  isWinner = False
  isLoser = False

  while isWinner == False and isLoser == False:
    choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ')
    userChoice = int(choice)
    computerChoice = random.randint(0, 2)

    showChoice(userChoice)

    print('Computer chose:')

    showChoice(computerChoice)

    if userChoice == 0:
      if computerChoice == 2:
        isWinner = True
      elif computerChoice == 1:
        isLoser = True
    elif userChoice == 1:
      if computerChoice == 0:
        isWinner = True
      elif computerChoice == 2:
        isLoser = True
    else:
      if computerChoice == 0:
        isLoser = True
      elif computerChoice == 1:
        isWinner = True

    if isLoser:
      print('You lose!')
    elif isWinner:
      print('You win!')
    else:
      print('It\'s a tie, play again')

def showChoice(c):
  if c == 0:
    print(rock)
  elif c == 1:
    print(paper)
  elif c == 2:
    print(scissors)
  else:
    print('Invalid choice')

playGame()