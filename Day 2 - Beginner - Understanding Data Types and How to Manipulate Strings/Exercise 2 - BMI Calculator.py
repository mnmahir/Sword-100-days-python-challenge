# 6 + 2   # Addition
# 6 - 2   # Substraction
# 6 * 2   # Multiplication
# 6 / 2   # Division (Always result in float)
# 6 ** 2  # Power

# # PEMDAS (Left to right)
# 3 * 3 + 3 / 3 - 3
# print(3 * 3 + 3 / 3 - 3)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(weight)/float(height)**2
print(int(BMI))