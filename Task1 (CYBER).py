def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around if needed
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # Non-alphabetic characters remain unchanged
    return encrypted_message


def caesar_cipher_decrypt(message, shift):
    return caesar_cipher_encrypt(message, -shift)  # Decryption is reverse encryption


def main():
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1 or 2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the shift value.")
        return
    
    if choice == '1':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == '2':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()