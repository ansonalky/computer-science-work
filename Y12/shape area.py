#DECLARE length, base, height, radius:INTEGER
#DECLARE Area:FLOAT
#DECLARE Shape:STRING

shape=input("Enter the shape:")

def square():
    length=int(input("Enter the length of a side:"))
    area=float(length * length)
    print("The area of the square is", area)

def triangle():
    base=int(input("Enter the length of base:"))
    height=int(input("Enter the length of height:"))
    area=float((base*height)/2)
    print("The area of the triangle is", area)

def circle():
    radius=int(input("Enter the length of radius:"))
    area=float(3.141592654*radius*radius)
    print("The area of the circle is", area)

if shape == "Square" or shape == "square":
    square()
elif shape == "Triangle" or shape =="triangle":
    triangle()
elif shape == "Circle" or shape =="circle":
    circle()
else:
    print ("This shape is not valid in this program")