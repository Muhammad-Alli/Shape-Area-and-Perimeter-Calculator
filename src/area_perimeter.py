import math

def square_area(length):
    return length * length

def square_perimeter(length):
    return length * 4

def calc_rectangle(l, b):
    area = l * b
    perimeter = 2 * (l + b)
    return area, perimeter

def calc_circle(r):
    area = math.pi * r * r
    perimeter = 2 * math.pi * r
    return area, perimeter

def calc_triangle(b, h):
    area = 0.5 * b * h
    c = math.sqrt(b ** 2 + h ** 2)
    perimeter = c + b + h
    return area, perimeter
