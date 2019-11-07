

def decimal_to_binary(n):
    bit_8 = 0
    bit_7 = 0
    bit_6 = 0
    bit_5 = 0
    bit_4 = 0
    bit_3 = 0
    bit_2 = 0
    bit_1 = 0
    while n > 0:
        
        if n >= 128:
            n -= 128
            bit_8 = 1
            
        elif n >= 64:
            n -= 64
            bit_7 = 1
            
        elif n >= 32:
            n -= 32
            bit_6 = 1
            
        elif n >= 16:
            n -= 16
            bit_5 = 1

        elif n >= 8:
            n -= 8
            bit_4 = 1

        elif n >= 4:
            n -= 4
            bit_3 = 1

        elif n >= 2:
            n -= 2
            bit_2 = 1

        elif n >= 1:
            n -= 1
            bit_1 = 1

    print(bit_8, bit_7, bit_6, bit_5, bit_4, bit_3, bit_2, bit_1)



    
    

running = True


print("welcome to the decimal to binary converter")


while running:
    
    num = int(input("Enter the number you wish to convert (no bigger than 255): "))
    decimal_to_binary(num)
