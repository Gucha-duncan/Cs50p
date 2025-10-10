words = {'PAIR':4, 'HAIR':4, 'CHAIR':5}

def main():
    
    print("Welcome to Spelling Bee!")
    print("Your letters are: AIPCHRHG")
    
    while len(words) > 0:
        print(f"{len(words)} words left!")
        guess = input("Guess a word: ").upper()
        
        if guess == 'GRAPHIC':
            words.clear()
            print("You have won the game by guessing super word!")
        
        elif guess in words.keys():
            score = words.pop(guess)
            print(f"Congratulations you have scored {score} points!")
            
    print('That is the game!')
            
          
            
           

    
    

    
main()