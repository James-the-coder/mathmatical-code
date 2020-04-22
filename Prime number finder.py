"""Prime Number Finder"""

a = 1
prime = False
while True:
    
    while a == 1:
        number = input("Enter the number: ")
        try:
            number = int(number)
            a += 1
        except ValueError:
            print("That is not an integer")
    if number > 1:
        for i in range(2,number):
            
            if (number%i)== 0:
                prime = False
                break
            else:
                prime = True

        if prime == True:
            print("Prime")
            a=1
        
        else:
            print("Not Prime")
            a = 1
        
    else:
        print("not prime")
        a = 1
            
        

    
