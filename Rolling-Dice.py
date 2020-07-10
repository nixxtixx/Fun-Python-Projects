import random

roll = input("Have you rolled the dice? ")

while (roll == "yes") or (roll == "Yes") or (roll == "y"):
  print("Rolling...")
  print("Your first roll is " + str(random.randint(1,6)))

  roll = input("Roll again? ")

if (roll == "No") or (roll == "no") or (roll == "n"):
  print("Ok, come back again soon!")
else:
  print("Invalid Response")
  roll = input("Try again? ")
