"""Welcome to the decimal to binary converter"""

bits = []
running = True

def decimal_binary(n, b):
    counter = 0
    z = len(b)
    while n > 0:
        """binary uses powers of 2 so i have taken the length of the list - 1 to
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

    bit = input("Enter the number of bits: ")

    if bit == "q":
        running = False
        quit()
        
    num = input("Enter the number: ")

    if num == "q":
        running = False
        quit()

    

    bit = int(bit)
    num = int(num)

    for i in range(bit):
        bits.append("0")



    print(decimal_binary(num, bits))
