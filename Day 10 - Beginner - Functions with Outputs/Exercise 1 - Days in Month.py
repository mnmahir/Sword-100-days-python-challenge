# def format_name(f_name, l_name):
#     """Take a first and last name and format it to return
#     the title case version of the name."""
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"


# formatted_string = format_name("MAhir", "seHMI")
# print(formatted_string)
# print(format_name("MAhir", "seHMI"))

# print(
#     format_name(input("What is your first name? "), input("What is your last name? "))
# )


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Take year and month and return number of days
    for that month in that year"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month"
    if is_leap(year):
        month_days[1] = 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
