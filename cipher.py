def encryption(message: str, key: int): 
    encrypted_message = "" 
    for letter in message: 
        if letter == " ": 
            encrypted_message += " " 
        elif letter == ".": 
            encrypted_message += "." 
        else: 
            index = capital_letters.index(letter.upper())
            if index + key > 25: 
                new_index = index + key - 25
                encrypted_message += capital_letters[new_index] 
            else: 
                new_index = index + key 
                encrypted_message += capital_letters[new_index] 
    print(encrypted_message) 

def decryption(message: str, key: int): 
    decrypted_message = ""
    for letter in message: 
        if letter == " ": 
            decrypted_message += " " 
        elif letter == ".": 
            decrypted_message += "." 
        else: 
            index = capital_letters.index(letter.upper()) 
            if index - key < 0: 
                new_index = index - key + 25
                decrypted_message += capital_letters[new_index].lower() 
            else: 
                new_index = index - key
                decrypted_message += capital_letters[new_index].lower() 
    print(decrypted_message)
    
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print("The cipher can encrypt or decrypt messages.") 
print("This program takes a key, which is used to encrypt/decrypt messages by shifting each letter in the message in left/right direction positionally.") 
print()

user_choice = input("Encrypt: e, Decrypt: d = ") 
if user_choice == 'e' or user_choice == "E": 
    key = int(input("Key: ")) 
    if key > 25 or key < 0:  
        raise ValueError
    else: 
        to_encrypt = input("Message: ")
        encryption(to_encrypt, key)  

elif user_choice == "d" or user_choice == "D": 
    key = int(input("Key: "))  
    if key > 25 or key < 0: 
        raise ValueError 
    else: 
        to_decrypt = input("Message: ") 
        decryption(to_decrypt, key) 


