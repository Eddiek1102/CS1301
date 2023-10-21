import random 

print("I am thinking of a 3-digit number between 000 and 999.")
print("Try to guess what it is.") 
print("Here are some clues: ") 
print("When I say:              That means:")
print("  Pico                     One digit is correct but in the wrong position") 
print("  Fermi                    One digit is correct and in the right position")
print("  Bagels                   No digit is correct")
print("I have thought of a number.")
print("You have 10 guesses to correctly guess that number...") 

random_number = random.randint(0, 999)
random_number_string = str(random_number) 
guess_counter = 1
#print(f"Correct answer: {random_number}")

while True:  
    if guess_counter == 11: 
        print("Game over: You've run out of guesses.") 
        print(f"Correct answer was {random_number}")
        break 
    
    guess = int(input(f"Guess #{guess_counter}: "))
    guess_string = str(guess) 
    
    #Correct guess: 
    if guess == random_number: 
        print("You got it!") 
        break 
    
    pico_counter = 0 
    fermi_counter = 0 
    for i in range(0, len(guess_string)): 
        if guess_string[i] == random_number_string[i]: 
            fermi_counter += 1 
        elif guess_string[i] != random_number_string[i]: 
            if guess_string[i] in random_number_string: 
                pico_counter += 1 
    if pico_counter == 0 and fermi_counter == 0: 
        print("Bagels", end="") 
    else: 
        print("Pico " * pico_counter, end="")
        print("Fermi " * fermi_counter, end="")
    print() 
        
    guess_counter += 1 
