counter = 1

running = True

while running:
    table = int(input("What times table do you want?: "))
    for i in range(12):
        total = counter * table
        print(str(counter) +" x "+str(table)+" = "+str(total))
        counter += 1
    counter = 1
