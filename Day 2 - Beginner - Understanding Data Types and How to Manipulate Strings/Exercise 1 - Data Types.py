# # Data Types

# # String
# print("Hello"[4])   # Subscripting

# # Integer
# print(123 + 456)
# print(123_456_789)  # Underscore act as comma for human to understand.

# # FLoat
# print(123_456.7)

# # Boolean

# print(True)
# False

# #Type error
# num_char = len(input("What is your name? "))
# # print("Your name has " + num_char + " characters.")
# print(type(num_char))                                    # Use type to investigate type of data
# print("Your name has " + str(num_char) + " characters.") # Type casting

# print(10 + float("23.4"))

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))
