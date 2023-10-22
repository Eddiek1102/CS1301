bitmap = """
            ***********     **  *****        ** 
            **** **              **         *  
            * ********** ***   ******  ***    *
            ****          ******         *      
            *****         ******          *** * 
            ****     **      *****     ***   * 
            ***********************************
                                               
             ***** *            ****      **   
            *******         *         * *******"""
row_length = 35
message = input("Enter the message you'd like to represent on a bitmap: ") 
message_arr = [] 
for i in range(0, len(message)): 
    message_arr.append(message[i])

element_counter = 0
message_counter = 0 

bitmap_message = [] 

for i in range(0, len(bitmap)):
    if bitmap[i] == "*": 
        bitmap_message.append(message_arr[message_counter])
        message_counter += 1 
        if message_counter == len(message) - 1: 
            message_counter = 0 
    elif bitmap[i] == " " or bitmap[i] == "": 
        bitmap_message.append(" ") 

element_counter = 0 
for element in bitmap_message: 
    print(element, end= " ")
    element_counter += 1 
    if element_counter == 35: 
        print() 
        element_counter = 0 
print() 