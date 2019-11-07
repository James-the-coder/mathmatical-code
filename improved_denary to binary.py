

bits = []
running = True

def decimal_binary(n, b):
    counter = 0
    z = len(b)
    while n > 0:
        if n >= 2**(z-1):
            n -= 2**(z-1)
            b[counter] = 1
            if counter != len(b):
                counter += 1
            if z != 0:
                z -= 1

        else:
            if z != 0:
                z -= 1
                counter += 1
    return b


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
        bits.append(0)



    print(decimal_binary(num, bits))
