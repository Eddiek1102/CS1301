import random 

print("Guess a number from 0 to 10 inclusive.")
print("Your character will race a computer generated opponent.")
print("The closer your guess is to the true number, the more steps you will take per turn.")

correct_number = random.randint(0, 10)

bot = 'B' 
user = input("Pick a character: ") 
race_length = int(input("How many steps should the race length be? (Pick Between 10-50): ")) 

bot_track = [] 
user_track = [] 

for i in range(0, race_length, 1): 
    bot_track.append("") 
    user_track.append("") 

bot_index = 0 
user_index = 0 

bot_track[bot_index] = bot 
user_track[user_index] = user 

while True: 
    print("B: ", end = "")
    print(bot_track) 
    print(f"{user}: ", end ="")
    print(user_track) 
    
    bot_guess = random.randint(0, 10)
    user_guess = int(input("Guess a number: ")) 
    
    if bot_guess == correct_number: 
        bot_index += correct_number
    else: 
        bot_index += abs(correct_number - bot_guess) 

    if user_guess == correct_number: 
        user_index += correct_number 
    else: 
        user_index += abs(correct_number - user_guess) 
    
    if bot_index >= race_length and user_index >= race_length: 
        print("Draw.") 
        print(f"The correct number was {correct_number}")
        break 
    elif bot_index >= race_length: 
        print("You Lose.") 
        print(f"The correct number was {correct_number}")
        break 
    elif user_index >= race_length: 
        print("You Win!") 
        print(f"The correct number was {correct_number}")
        break 
    else: 
        bot_track.clear() 
        user_track.clear() 
        for i in range(0, race_length, 1): 
            bot_track.append("") 
            user_track.append("") 
        bot_track[bot_index] = bot 
        user_track[user_index] = user 
        
