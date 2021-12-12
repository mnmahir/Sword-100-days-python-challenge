alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(ori_text, shift_amount, direction):
    out_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in ori_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            while new_position > (len(alphabet) - 1):
                new_position -= len(alphabet)
            out_text += alphabet[new_position]
        else:
            out_text += char
    print(f"The {direction}d text is {out_text}")


from art import logo

print(logo)

program_run = True

while program_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(ori_text=text, shift_amount=shift, direction=direction)

    result = input(
        "Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'. "
    ).lower()

    if result == "no":
        program_run = False
        print("Goodbye!")
