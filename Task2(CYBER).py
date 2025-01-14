from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    
    # Convert image to numpy array for faster pixel manipulation
    img_array = np.array(img)
    
    # Ensure key length matches the number of color channels (e.g., 3 for RGB)
    key = np.array(list(key))  # Convert key to numpy array for element-wise operations
    
    # Encrypting each pixel
    encrypted_data = np.bitwise_xor(img_array, key)
    
    # Create encrypted image from numpy array
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'), img.mode)
    
    # Save encrypted image
    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(input_image_path)
    
    # Convert image to numpy array for faster pixel manipulation
    encrypted_img_array = np.array(encrypted_img)
    
    # Ensure key length matches the number of color channels (e.g., 3 for RGB)
    key = np.array(list(key))  # Convert key to numpy array for element-wise operations
    
    # Decrypting each pixel
    decrypted_data = np.bitwise_xor(encrypted_img_array, key)
    
    # Create decrypted image from numpy array
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'), encrypted_img.mode)
    
    # Save decrypted image
    decrypted_image.save(output_image_path)

# Example usage
input_image = "input_image.jpg"  # Path to your original image
encrypted_image = "encrypted_image.jpg"  # Path where the encrypted image will be saved
decrypted_image = "decrypted_image.jpg"  # Path where the decrypted image will be saved
encryption_key = b'MySecretKey'  # Encryption key as bytes

# Encrypt image
encrypt_image(input_image, encrypted_image, encryption_key)

# Decrypt image
decrypt_image(encrypted_image, decrypted_image, encryption_key)


