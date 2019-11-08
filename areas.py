
running = True


def area_circle(n):
    pi = 3.14159
    area = pi * (n**2)
    print(area)



def area_rectangle(x,y):
    area = x*y
    print(area)



def area_square(n):
    area = n**2
    print(area)


def area_right_angle_triangle(x,y):
    area = x*y*0.5
    print(area)


def area_isosceles_tri(x,y):
    area = x*y
    print(area)



def area_trapezium(x,y,z):
    area = (x+y)*0.5*z
    print(area)



print("you can calculate the area of a circle, rectangle, square, traingle or trapezium")
while running:
    
    shape = input("Enter the shape you would like to calculate the area for: ")

    if shape == "circle":
        radius = float(input("Enter the radius: "))
        area_circle(radius)


    elif shape == "square":
        side = float(input("Enter the length of a side: "))
        area_square(side)

    elif shape == "rectangle":
        side_1 = float(input("Enter the length of one side: "))
        side_2 = float(input("Enter the length of the other side: "))
        area_rectangle(side_1,side_2)


    elif shape == "triangle":
        type_tri = input("Enter the type of triangle [isosceles or right_angle]: ")
        if type_tri == "isosceles":
            height = float(input("Enter the height: "))
            length = float(input("Enter the length: "))
            area_isosceles_tri(height,length)

        elif type_tri == "right_angle":
            height_right = float(input("Enter the height: "))
            length_right = float(input("Enter the length: "))
            area_right_angle_triangle(height_right,length_right)

        else:
            print("did you mean isosceles or right_angle?")
            
            


    elif shape == "trapezium":
        length_1 = float(input("Enter the first length: "))
        length_2 = float(input("Enter the second length: "))
        height_t = float(input("Enter the height: "))
        area_trapezium(length_1,length_2,height_t)

    elif shape == "q":
        running = False

    else:
        print("invalid option")
