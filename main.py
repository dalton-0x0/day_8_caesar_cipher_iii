from art import logo_1

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    # loop through each character in the start text
    for char in start_text:
        # the user enters a number/symbol/space not in aplhabet
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo_1)
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # check if user made a valid 'direction' input
    if direction != 'encode' and direction != 'decode':
        print("Invalid cipher choice, type 'encode' or 'decode'. Goodbye!")
        exit()

    # text inputs
    text = input("Type your message:\n").lower()

    # shift with correction for if the user enters
    # a shift vaule greater than the number of letters in the alphabet
    shift = int(input("Type the shift number:\n")) % 26

    caesar_cipher(start_text=text,
                  shift_amount=shift,
                  cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if restart == "no":
        should_end = True
        print("Goodbye!")
