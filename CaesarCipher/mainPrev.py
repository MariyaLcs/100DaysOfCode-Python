# First Part
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text, shift):
    cipher_text=""
    for letter in text:
        idx = alphabet.index(letter)
        cipher_text+=alphabet[idx+shift]
   
encrypt(text, shift)

#Second part
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    plain_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The encoded text is {plain_text}")

if direction=='encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction=='decode':
    decrypt(plain_text=text, shift_amount=shift)

#Third part Reorganising Code

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, direction):
    end_text = ""
    if direction=='decode':
            shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)             
        new_position = position + shift_amount
        end_text+=alphabet[new_position]
    print(f"The {direction}d text is \n{end_text}")

caesar(start_text=text, shift_amount=shift, direction=direction)