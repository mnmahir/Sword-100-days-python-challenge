# capitals = {"France": "Paris", "Germany": "Berlin"}

# # Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "lille", "Dijon"], "total_visits": 12},
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     },
# }

# # Nesting Dictionary in a List
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "lille", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     },
# ]

travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new = {}
    new["country"] = country
    new["visits"] = visits
    new["cities"] = cities
    travel_log.append(new)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
