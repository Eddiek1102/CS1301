class Sevenseg: 
    def __init__(self, first: int, second: int, third: int, fourth: int, fifth: int, sixth: int, seventh: int):
        init_arr = [abs(first), abs(second), abs(third), abs(fourth), abs(fifth), abs(sixth), abs(seventh)] 
        self.sevenseg_arr = [] 
        for digit in init_arr: 
            if digit >= 0 and digit <= 9: 
                if digit == 0: 
                    row1 = " __ " 
                    row2 = "|  |"
                    row3 = "|__|"
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 1: 
                    row1 = "    "
                    row2 = "   |" 
                    row3 = "   |" 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 2: 
                    row1 = " __ " 
                    row2 = " __|"
                    row3 = "|__"
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 3: 
                    row1 = " __ "
                    row2 = " __|"
                    row3 = " __|" 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 4: 
                    row1 = "    " 
                    row2 = "|__|"
                    row3 = "   |" 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 5: 
                    row1 = " __ " 
                    row2 = "|__ "
                    row3 = " __|" 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 6: 
                    row1 = " __   " 
                    row2 = "|__ "
                    row3 = "|__|" 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 7: 
                    row1 = " __ " 
                    row2 = "   |" 
                    row3 = "   |" 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 8: 
                    row1 = " __ "
                    row2 = "|__|"
                    row3 = "|__|" 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                elif digit == 9: 
                    row1 = " __ "
                    row2 = "|__|" 
                    row3 = "   |" 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
                else: 
                    row1 = "    " 
                    row2 = " -- " 
                    row3 = "    " 
                    digit_arr = [row1, row2, row3] 
                    self.sevenseg_arr.append(digit_arr) 
    
    def __str__(self): 
        for digit in self.sevenseg_arr: 
            for row in digit: 
                print(row) 
        return 0

if __name__ == "__main__": 
    one_two_three_four_five_six_seven = Sevenseg(1, 2, 3, 4, 5, 6, 7) 
    print(one_two_three_four_five_six_seven) 
    
