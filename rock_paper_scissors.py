import random 

pone_score = 0 
ptwo_score = 0 

options = ["rock", "paper", "scissors"] 
r_counter = 0 
p_counter = 0 
s_counter = 0  

while True:
    pone_move = input("Enter 'rock', 'paper', or 'scissors' ('end' to quit): ")
    if pone_move.lower() == "end": 
        print("Game Terminated") 
        break 
    ptwo_move = options[random.randint(0, 2)]
    print(f"Player two has chosen {ptwo_move}")
    
    if pone_move.lower() == "rock": 
        r_counter += 1 
    elif pone_move.lower() == "paper": 
        p_counter += 1 
    elif pone_move.lower() == "scissors": 
        s_counter += 1 
    
    if ptwo_move.lower() == "rock": 
        r_counter += 1 
    elif ptwo_move.lower() == "paper": 
        p_counter += 1 
    elif ptwo_move.lower() == "scissors": 
        s_counter += 1 

    if pone_move.lower() == "rock" and ptwo_move.lower() == "paper": 
        ptwo_score += 1 
        print("Winner: Player 2") 
    elif pone_move.lower() == "rock" and ptwo_move.lower() == "scissors": 
        pone_score += 1 
        print("Winner: Player 1")
    elif pone_move.lower() == "rock" and ptwo_move.lower() == "rock": 
        pone_score += 0 
        ptwo_score += 0 
        print("Winner: None") 
    elif pone_move.lower() == "paper" and ptwo_move.lower() == "scissors": 
        ptwo_score += 1 
        print("Winner: Player 2") 
    elif pone_move.lower() == "paper" and ptwo_move.lower() == "rock": 
        pone_score += 1 
        print("Winner: Player 1")
    elif pone_move.lower() == "paper" and ptwo_move.lower() == "paper": 
        pone_score += 1 
        ptwo_score += 1 
        print("Winner: None") 
    elif pone_move.lower() == "scissors" and ptwo_move.lower() == "rock": 
        ptwo_score += 1 
        print("Winner: Player 2") 
    elif pone_move.lower() == "scissors" and ptwo_move.lower() == "paper": 
        pone_score += 1 
        print("Winner: Player 1")
    elif pone_move.lower() == "scissors" and ptwo_move.lower() == "scissors": 
        pone_score += 1 
        ptwo_score += 1 
        print("Winner: None") 
    print() 
    
print("Final Scores: ") 
print("-" * len("Final Scores:"))
print(f"Player 1: {pone_score}")
print(f"Player 2: {ptwo_score}")
print() 

print("Results: ") 
print("-" * len("Results:"))
if pone_score > ptwo_score: 
    print("Player One is the winner!")
elif pone_score < ptwo_score: 
    print("Player Two is the winner!")
else: 
    print("The game is a draw") 
print() 

print("Game Statistics: ")
print("-" * len("Game Statistics:"))
print(f"Rock was playerd {r_counter} times") 
print(f"Paper was played {p_counter} times") 
print(f"Scissors was played {s_counter} times") 
 

    