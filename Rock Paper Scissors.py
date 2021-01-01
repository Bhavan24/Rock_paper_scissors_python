import emoji
import random

rock = "\N{raised fist}"
paper = "\N{raised hand}"
scissors = "\N{victory hand}"
choice_list = [rock,paper,scissors]

bar = "--------------------"

print('''
+-----------------------+
| Rock Paper Scissors	|
+-----------------------+
| 1.rock		|
| 2.paper		|
| 3.scissors		|
+-----------------------+''')

selection = "y"
while selection == "y":
	pc = random.choice(choice_list)	

	try:
		user = int(input("Enter your choice: "))
	except:
		user = print("Please enter a number")
		continue	

	print(bar)

	if user == 1:
		user_input = rock
		print("Your choice: " + rock)
	elif user == 2:
		user_input = paper
		print("Your choice: " + paper)
	elif user == 3:
		user_input = scissors
		print("Your choice: " + scissors)
	else:
		print("Please enter a valid number")
		continue

	print("Computer choice: ", pc)
	print(bar)

	if (user_input == paper and pc == rock):
		print("You won!")
	elif (user_input == rock and pc == scissors):
		print("You won!")
	elif (user_input == scissors and pc == paper):
		print("You won!")
	elif (user_input == pc):
		print("Draw!")
	else:
		print("You Lost!")

	print(bar)
	selection = input("Play again? (y/n): ")
	print(bar)
