# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
# }

# # Retrieving items from dictionary.
# print(
#     programming_dictionary["Bug"]
# )  # Wrong spelling or key not in dictionary leads to key error.

# # Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# empty_dictionary = {}
# print(empty_dictionary)
# empty_dictionary["Test"] = "Hello"
# print(empty_dictionary)

# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(f"{key} is {programming_dictionary[key]}")

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)
