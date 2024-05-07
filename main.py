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

#Write your code below this line 👇
game_image = [rock, paper, scissors]

choice = int(input("What do you choose? type 0 for Rock, 1 for paper or 2 for Scissors. \n"))
if choice >=3 or choice <0:
  print("You type an invalid number, you lose!")

else:
  print(game_image[choice])
  print(" Computer Chose:")

  random_num = random.randint(0,2)
  machine_choice = random_num
  print(game_image[machine_choice])
  
  if choice == machine_choice:
    print("draw")
  elif choice == 0 and machine_choice == 1:
    print("You lose")
  elif choice == 0 and machine_choice == 2:
    print("You Win")
  elif choice == 1 and machine_choice == 0:
    print("You win")
  elif choice == 1 and machine_choice == 2:
    print("You Lose")
  elif choice == 2 and machine_choice == 0:
    print("You lose")
  elif choice == 2 and machine_choice == 1:
    print("You Win")

