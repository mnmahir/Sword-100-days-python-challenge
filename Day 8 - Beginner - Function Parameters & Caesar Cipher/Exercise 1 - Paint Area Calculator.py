# # Review:
# # Create a function called greet().
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.


# def greet():
#     print("Hello!")
#     print("How do you do?")
#     print("Isn't the weather nice today?")


# greet()


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# greet_with_name("Mahir")


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")


# greet_with("Mahir", "Kuala Lumpur")
# greet_with(location="London", name="Mahir")

import math

# Write your code below this line 👇
def paint_calc(height, width, cover):
    num_of_cans = math.ceil(height * width / cover)
    print(f"You'll need {num_of_cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
