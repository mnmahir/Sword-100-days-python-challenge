################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# # Local Scope
# def drink_potion():
#     portion_stregth = 2
#     print(portion_stregth)
# drink_potion()
# print(porion_stregth) # Will get wrror because variable not available.

# Global Scope
# player_health = 10

# def drink_potion():
#     potion_stregth = 2
#     print(player_health)

# drink_potion()
# print(player_health)

# # there is no Block Scope

# game_level = 3


# Modifying Global Scope
enemies = 1


def increase_enemies():
    global enemies          # Variable with global is prone to fail because we might accidently edit. We can use return instead.
                            # But Global constants can be useful
    enemies += 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Global constants - usually written in UPPERCASE
PI = 3.14159
URL = "https://mahirsehmi.me"
YOUTUBE_HANDLE = "Mahir Sehmi"