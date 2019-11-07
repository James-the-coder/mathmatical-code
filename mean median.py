


numList = []
total = 0
running = True

def median(n):
    if len(n) % 2 == 0:
        mid = len(n) // 2
    else:
        mid = (len(n)+1)//2
    return n[mid-1]

def mean(x, n):
    mean = x // len(n)
    return mean



while running:
    loops = int(input("How many numbers do you want to enter?: "))
    for i in range(loops):
        num = int(input("Enter a number: "))
        total += num
        numList.append(num)

    print("The median is "+str(median(numList)))
    print("The mean is "+str(mean(total, numList)))
    
    
    
