alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, placement):
    cipher_text = ""
    for i in plain_text:
        position = alphabet.index(i)
        new_position = position + placement
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(plain_text, placement):
    cipher_text = ''
    for i in plain_text:
        position = alphabet.index(i)
        new_position = position - placement
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The decoded text is {cipher_text}")


if direction == 'encode':
    encrypt(text, shift)
if direction == 'decode':
    decrypt(text, shift)

