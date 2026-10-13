# Calculate the Area of a Circle

def get_area_of_circle(r):
    PI = 3.14
    area_of_circle = PI * r**2
    return area_of_circle

radius = int(input("Enter your radius : "))
res = get_area_of_circle(radius)
print("Area of circle is : ",res)