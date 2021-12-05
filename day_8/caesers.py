alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesers(encryption, cipher_text, shift_ammount):
    if encryption == 'encode':
        cipher_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position + shift_ammount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    else:
        plain_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_ammount
            plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")


caesers(direction, text, shift)
