'''
Name: Sachkerat Singh Matharoo
Student ID: 100996938
Course: TPRG 2131 - Programming for Technology II
Assignment 1 - Area/Volume Calculator
Date: Oct 17, 2024

Description: This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving
credit to the original author(s).

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

The program can show results in two views:
- V/v : calculated view (shows the equation and answer)
- D/d : Default view (shows only the answer)
'''

import math  # Import math for π (pi) and powers

print("********* A/V Calculator *********")

# ----------------------------------------------------
# Calculation Functions
# ----------------------------------------------------

def area_circle(radius):
    """Calculate area of a circle = π * r²"""
    area = math.pi * radius ** 2
    return round(area, 1)

def vol_cylinder(radius, height):
    """Calculate volume of a cylinder = π * r² * h"""
    volume = math.pi * radius ** 2 * height
    return round(volume, 1)

def area_rectangular(length, width):
    """Calculate area of a rectangle = length * width"""
    area = length * width
    return round(area, 1)

def vol_sphere(radius):
    """Calculate volume of a sphere = (4/3) * π * r³"""
    volume = (4 / 3) * math.pi * radius ** 3
    return round(volume, 1)

def area_triangle(base, height):
    """Calculate area of a triangle = 0.5 * base * height"""
    area = 0.5 * base * height
    return round(area, 1)


# ----------------------------------------------------
# Input Validation Functions
# ----------------------------------------------------

def get_valid_input(message):
    """Ask user for a positive number. Repeats until valid."""
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            else:
                print("The value must be greater than zero.")
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

def get_valid_string(message):
    """Ask user for Q/q, V/v, or D/d. Repeats until valid."""
    while True:
        value = input(message).strip()
        if value in ['q', 'Q', 'v', 'V', 'd', 'D']:
            return value
        else:
            print("Invalid input. Please enter Q/q, V/v, or D/d.")


# ----------------------------------------------------
# Result Display Function
# ----------------------------------------------------

def display_result(formula, result, mode):
    """Display result based on view selection (V or D)."""
    if mode.lower() == "v":
        return f"Equation: {formula}\nAnswer: {result}"
    else:
        return f"Answer: {result}"


# ----------------------------------------------------
# Main Program
# ----------------------------------------------------

if __name__ == "__main__":

    while True:
        # Level 0 Menu - Choose view mode
        user_choice = get_valid_string(
            "\nEnter Q/q to quit, V/v for calculated view, or D/d for default view:\n[Q/V/D] → "
        )

        if user_choice.lower() == "q":
            print("\nExiting program. Have a nice day!")
            break

        # Level 1 Menu - Choose calculation type
        while True:
            print("\n*********")
            print("1. Area of a Circle")
            print("2. Volume of a Cylinder")
            print("3. Area of a Rectangle")
            print("4. Volume of a Sphere")
            print("5. Area of a Triangle")
            print("6. Main Menu")
            print("*********")

            choice = input("Select option (1–6): ")

            # Option 1: Circle Area
            if choice == "1":
                radius = get_valid_input("Enter radius: ")
                result = area_circle(radius)
                formula = f"π * {radius}²"
                print(display_result(formula, result, user_choice), "㎠")

            # Option 2: Cylinder Volume
            elif choice == "2":
                radius = get_valid_input("Enter radius: ")
                height = get_valid_input("Enter height: ")
                result = vol_cylinder(radius, height)
                formula = f"π * {radius}² * {height}"
                print(display_result(formula, result, user_choice), "㎥")

            # Option 3: Rectangle Area
            elif choice == "3":
                length = get_valid_input("Enter length: ")
                width = get_valid_input("Enter width: ")
                result = area_rectangular(length, width)
                formula = f"{length} * {width}"
                print(display_result(formula, result, user_choice), "㎠")

            # Option 4: Sphere Volume
            elif choice == "4":
                radius = get_valid_input("Enter radius: ")
                result = vol_sphere(radius)
                formula = f"(4/3) * π * {radius}³"
                print(display_result(formula, result, user_choice), "㎥")

            # Option 5: Triangle Area
            elif choice == "5":
                base = get_valid_input("Enter base: ")
                height = get_valid_input("Enter height: ")
                result = area_triangle(base, height)
                formula = f"0.5 * {base} * {height}"
                print(display_result(formula, result, user_choice), "㎠")

            # Option 6: Return to main menu
            elif choice == "6":
                print("\nReturning to main menu...")
                break

            else:
                print("Invalid input. Please try again.")
