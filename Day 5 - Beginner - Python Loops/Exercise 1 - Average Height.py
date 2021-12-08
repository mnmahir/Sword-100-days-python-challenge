# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_height = 0
pax = 0

# sum_height = sum(student_heights)
# pax = len(student_heights)

for n in student_heights:
    sum_height += n
    pax += 1

average = round(sum_height/pax)

print(average)


