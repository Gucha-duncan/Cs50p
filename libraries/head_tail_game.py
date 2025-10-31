import random

coin  = random.choice(["head", "tail"])
user_choice = input("Enter head or tail to play the game:").strip().lower()


if user_choice == coin:
    print(f" Your choice '{user_choice}' is correct! Congratultions")
    
else:
    print("Not Correct! Try again !")

