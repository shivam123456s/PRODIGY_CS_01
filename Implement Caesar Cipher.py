#TASK 1
#Implement Caesar Cipher
#  Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
# Allow users to input a message and a shift value to perform encryption and decryption.
def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            # Shift and wrap around alphabet if necessary
            shifted_char = shift_char(char, shift)
            encrypted_message += shifted_char
        else:
            encrypted_message += char  # Keep non-letter characters unchanged
    return encrypted_message

def decrypt_message(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            # Reverse shift and wrap around alphabet if necessary
            shifted_char = shift_char(char, -shift)
            decrypted_message += shifted_char
        else:
            decrypted_message += char  # Keep non-letter characters unchanged
    return decrypted_message

def shift_char(char, shift):
    if char.isupper():  # Handle uppercase letters
        start = ord('A')
    elif char.islower():  # Handle lowercase letters
        start = ord('a')
    else:
        return char  # Non-alphabetical characters are returned unchanged

    # Calculate new shifted position, wrapping around using modulo
    new_pos = (ord(char) - start + shift) % 26 + start
    return chr(new_pos)

# Main program starts here
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

operation = input("Do you want to encrypt or decrypt the message? (e/d): ").lower()

if operation == "e":
    encrypted_message = encrypt_message(message, shift)
    print("Encrypted message:", encrypted_message)
elif operation == "d":
    decrypted_message = decrypt_message(message, shift)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice.")
