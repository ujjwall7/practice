def circle(radius:float) -> None:
    area = 3.14 * radius * radius
    print(f"Area of circle with radius {radius} = {area}")

def rectangle(length:float, breadth:float) -> None:
    print(f"Area of rectangle = {length * breadth}")

def triangle(base:float, height:float) -> None:
    print(f"Area of triangle = {0.5 * base * height}")



# x: int = 5
print(__name__)
if __name__=="__main__":   #this file name internally main,  agar is file la naam main hai tabhi circle and rectange run honge
    circle(45.52)
    rectangle(45.52,12)


