import sys 

print("Slot numbers: ") 
print("[1][2][3]\n[4][5][6]\n[7][8][9]\n")

class Tictactoe: 
    def __init__(self): 
        self.__first_row_board = [" ", " ", " "]
        self.__second_row_board = [" ", " ", " "] 
        self.__third_row_board = [" ", " ", " "]
        
    def print_board(self): 
        print("Current Board: ")
        print(self.__first_row_board) 
        print(self.__second_row_board) 
        print(self.__third_row_board, "\n")  
        
    def edit_first_row(self, choice: str, slot: int): 
        if slot in range(1, 4): 
            if self.__first_row_board[slot - 1] == " ": 
                self.__first_row_board[slot - 1] = choice
            else: 
                print("invalid slot") 
                return False 
        else: 
            raise ValueError("Slot is out of range") 
    
    def edit_second_row(self, choice: str, slot: int): 
        if slot in range(4, 7): 
            if self.__second_row_board[slot - 4] == " ": 
                self.__second_row_board[slot - 4] = choice 
            else: 
                print("invalid slot") 
                return False 
        else: 
            raise ValueError("Slot is out of range") 

    def edit_third_row(self, choice: str, slot: int): 
        if slot in range(7, 10): 
            if self.__third_row_board[slot - 7] == " ": 
                self.__third_row_board[slot - 7] = choice 
            else: 
                print("invalid slot")
                return False 
        else: 
            raise ValueError("Slot is out of range") 
    
    def check_game_status(self): 
        if self.__first_row_board[0] == self.__first_row_board[1] and self.__first_row_board[2] == self.__first_row_board[1]:
            if self.__first_row_board[0] == " ": 
                return True  
            return False 
        elif self.__first_row_board[0] == self.__second_row_board[0] and self.__third_row_board[0] == self.__second_row_board[0]:
            if self.__first_row_board[0] == " ": 
                return True  
            return False 
        elif self.__first_row_board[1] == self.__second_row_board[1] and self.__third_row_board[1] == self.__second_row_board[1]: 
            if self.__first_row_board[1] == " ": 
                return True 
            return False 
        elif self.__first_row_board[2] == self.__second_row_board[2] and self.__third_row_board[2] == self.__second_row_board[2]: 
            if self.__first_row_board[2] == " ": 
                return True 
            return False 
        elif self.__first_row_board[0] == self.__second_row_board[1] and self.__third_row_board[2] == self.__second_row_board[1]: 
            if self.__first_row_board[0] == " ": 
                return True 
            return False 
        elif self.__first_row_board[2] == self.__second_row_board[1] and self.__third_row_board[0] == self.__second_row_board[1]: 
            if self.__first_row_board[2] == " ": 
                return True 
            return False 
        elif self.__second_row_board[0] == self.__second_row_board[1] and self.__second_row_board[1] == self.__second_row_board[2]: 
            if self.__second_row_board[0] == " ": 
                return True 
            return False 
        elif self.__third_row_board[0] == self.__third_row_board[1] and self.__third_row_board[2] == self.__third_row_board[1]: 
            if self.__third_row_board[0] == " ": 
                return True 
            return False 
        return True 

if __name__ == "__main__": 
    game = Tictactoe() 
    i = 1
    while game.check_game_status() == True : 
        game.print_board() 
        
        print(f"Turn {i}:")
        choice = str(input("Enter a 'x' or 'o': "))
        slot = int(input("Enter slot number: ")) 
        if slot in range(1, 4): 
            game.edit_first_row(choice, slot) 
        elif slot in range(4, 7): 
            game.edit_second_row(choice, slot) 
        elif slot in range(7, 10): 
            game.edit_third_row(choice, slot) 
        i += 1 
    game.print_board() 
    sys.exit() 
