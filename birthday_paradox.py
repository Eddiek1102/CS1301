import random, datetime 

num_birthdays = int(input("How many birthdays should I generate? "))

def make_birthdays(num_birthdays: int): 
    birthdays = [] 
    for i in range(0, num_birthdays): 
        random_year = random.randint(1900, 2023) 
        random_month = random.randint(1, 12) 
        random_day = random.randint(1, 28) 
        birthday = datetime.date(random_year, random_month, random_day) 
        birthdays.append(birthday) 
    return birthdays 

def same_birthdays(birthdays: list):
    same_birthday_counter = 0 
    birthdays_only_once = []  
    for birthday in birthdays: 
        if birthday not in birthdays_only_once: 
            birthdays_only_once.append(birthday) 
        elif birthday in birthdays_only_once: 
            same_birthday_counter += 1 
    return same_birthday_counter 
    
print("Let us run 100 simulations...") 
total = 0 
for i in range(0, 100): 
    number_same_birthdays = same_birthdays(make_birthdays(num_birthdays)) 
    total += number_same_birthdays 
print(f"Out of 100 simulations of {num_birthdays} people, there were {total} matching birthdays!")
probability = (float(total) / float(100 * 100))
print(f"This means that {num_birthdays} people have a {probability}% chance of having a matching birthday in their group.") 
print("This is probabilty more than you would think!") 
print() 
print("Now, let's do 1000 simulations...")
total2 = 0 
for i in range(0, 1000): 
    number_same_birthdays2 = same_birthdays(make_birthdays(num_birthdays)) 
    total2 += number_same_birthdays 
print(f"Out of 1000 simulations of {num_birthdays} people, there were {total2} matching birthdays!")
probability2 = (float(total2) / float(1000 * 100)) 
print(f"This means that {num_birthdays} people have a {probability2}% chance of having a matching birthday in their group.")
print("This is probably more than you would think!") 