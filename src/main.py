import area_perimeter

while True:
    shape = input("Please enter the shape you want the area and perimeter calculated for: ")

    if shape.lower() == "square":
        length = float(input("Please enter the length of the square in meters: "))
        area = area_perimeter.square_area(length)
        perimeter = area_perimeter.square_perimeter(length)
        break
    elif shape.lower() == "rectangle":
        length = float(input("Please enter the length of the rectangle in meters: "))
        width = float(input("Please enter the width of the rectangle in meters: "))
        area, perimeter = area_perimeter.calc_rectangle(length, width)
        break
    elif shape.lower() == "circle":
        radius = float(input("Please enter the radius of the circle in meters: "))
        area, perimeter = area_perimeter.calc_circle(radius)
        break
    elif shape.lower() == "triangle":
        base = float(input("Please enter the base length of the right angled triangle in meters: "))
        height = float(input("Please enter the height of the right angled triangle in meters: "))
        area, perimeter = area_perimeter.calc_triangle(base, height)
        break
    else:
        print("Invalid shape selected")

print(f"The area and perimeter of the {shape} is:\narea = {round(area, 2)}m²\nperimeter = {round(perimeter, 2)}m")
