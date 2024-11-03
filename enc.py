def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged
            
    return result

# Example usage
if __name__ == "__main__":
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    if choice == 'e':
        encrypted_text = caesar_cipher(text, shift, mode="encrypt")
        print("Encrypted Text:", encrypted_text)
    elif choice == 'd':
        decrypted_text = caesar_cipher(text, shift, mode="decrypt")
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice! Please enter 'e' for encrypt or 'd' for decrypt.")