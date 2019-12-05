"""Welcome to the decimal to binary converter"""

import math


running = True

def decimal_binary(n, b):
    counter = 0
    z = len(b)
    while n > 0:
        """binary uses powers of 2 so i have taken the length of the list minus 1 to
           the power of two and minussed it from the number inputed"""
        if n >= 2**(z-1):
            n -= 2**(z-1)
            """I made it a string so I could get rid of the commas in the list when printed out"""
            b[counter] = "1"
            if counter != len(b):
                counter += 1
            if z != 0:
                z -= 1

        else:
            if z != 0:
                z -= 1
                counter += 1

    j = "".join(b)
    return j


while running:
    bits = []

   
        
    num = input("Enter the number: ")

    if num == "q":
        running = False
        quit()
    num = int(num)
    if num < 0:
        print("Must be positive integer")
        
    if num == 0:
        print("0")
    else:
        bit = int((math.log(num)/math.log(2))+1)
        

        for i in range(bit):
            bits.append("0")



        print(decimal_binary(num, bits))
