# Shape-Area-and-Perimeter-Calculator

A simple Python-based **command-line application** that calculates the **area** and **perimeter** of basic 2D shapes. The code is modular, separating shape-specific calculations into a dedicated module (`area_perimeter.py`) and uses user input (shape and parameter values) to interactively compute and display results.

---

## Features

- Calculates **area** and **perimeter** for user selectable shapes:
  - Square
  - Rectangle
  - Circle
  - Right-angled triangle
- Modular design using a reusable utility module (`area_perimeter.py`)
- Input validation for shape selection
- Results displayed with two decimal precision

---

## Getting Started

### Requirements
- Python 3.x

### Structure
  - main.py:  Main program for user interaction.
  - area_perimeter.py: Module containing shape-related functions.

### How to Run
On the terminal:
```bash
cd src
python main.py
```
---

## Usage Example

```
  Please enter the shape you want the area and perimeter calculated for: rectangle
  Please enter the length of the rectangle in meters: 5
  Please enter the width of the rectangle in meters: 3
  The area and perimeter of the rectangle is:
  area = 15.0m²
  perimeter = 16.0m
```
---

## Behind the Scenes

area_perimeter.py contains individual functions for:
  - square_area(length)
  - square_perimeter(length)
  - calc_rectangle(length, width)
  - calc_circle(radius)
  - calc_triangle(base, height) (right-angled only)

Each function returns either a single value (area/perimeter) or a tuple with both.
