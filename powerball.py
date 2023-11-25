#powerball 
import random 

class Money: 
    def __init__(self): 
        self.__balance = 0 
    
    def withdraw(self, amount: int):
        if self.__balance - amount >= 0: 
            self.__balance -= amount 
        else: 
            print("You don't have enough money to play!") 
    
    @property 
    def balance(self): 
        return int(self.__balance) 
    
    @balance.setter 
    def balance(self, amount: int): 
        if amount >= 0: 
            self.__balance += amount 
        else: 
            raise ValueError 

def main(): 
    print("Each powerball loterry ticket costs $2.00. The jackpot for this game is $1.586 billion!")
    print("It doesn't matter what the jackpot is, though, because the odds are not in your favor.")
    print("This simulation gives you the thrill of playing without wasting money.") 

    player = Money() 
    total_won = 0 
    total_lost = 0 
    
    num_tickets = int(input("How many tickets do you want to buy? ")) 
    print(f"This will cost ${num_tickets * 2}")
    
    if player.balance < (num_tickets * 2): 
        deposit = int(input(f"You need to deposit at least ${num_tickets * 2} to your account: "))
        player.balance = deposit 
    
    jackpot = [] 
    for i in range(0, 5, 1): 
        jackpot.append(random.randint(1, 26)) 
        
    for j in range(0, num_tickets): 
        player_nums = [] 
        for k in range(0, 5): 
            player_nums.append(random.randint(1, 26)) 
        if sorted(player_nums) == sorted(jackpot): 
            print(f"The winning numbers are {sorted(jackpot)}.", end = " ")
            print(f"Your numbers: {sorted(player_nums)}. YOU WON!") 
            total_won += 1586000000
        else:
            print(f"The winning numbers are {sorted(jackpot)}.", end = " ")
            print(f"Your numbers: {sorted(player_nums)}. YOU LOST.") 
            total_lost += 2 
    
    if total_won > total_lost: 
        print(f"You made money! \n You won ${total_won}!")
    else: 
        print(f"You wasted money! \n You wasted ${total_lost}")

if __name__ == "__main__": 
    main() 
    
            
            
                
