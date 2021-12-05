from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesers_cypher(encryption, normal_text, shift_ammount):
    if encryption == 'encode':
        cipher_text = ""
        for letter in normal_text:
            position = alphabet.index(letter)
            new_position = position + shift_ammount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    else:
        plain_text = ""
        for letter in normal_text:
            position = alphabet.index(letter)
            new_position = position - shift_ammount
            plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")

    repeat = input("Would you like to run this again? Yes / No\n")
    if repeat == 'Yes':
        caesers_cypher(direction, text, shift)
    if repeat == 'No':
        print('Have a nice day :)')
        exit(0)


caesers_cypher(direction, text, shift)
