import math

# ax2 + bx + c = 0

a = float(input("Input what A is: "))

b = float(input("Input what B is: "))

c = float(input("Input what C is: "))

d = (math.sqrt((b**2)-(4*a*c)))

solution_1 = ((-b+d)/2*a)
solution_2 = ((-b-d)/2*a)

print(d)

print("x is "+str(solution_1)+" or "+str(solution_2))
