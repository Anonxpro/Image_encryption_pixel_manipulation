import os
from PIL import Image
import numpy as np

def load_image(file_path):
    img = Image.open(file_path)
    return np.array(img)

def save_image(image_array, output_path):
    img = Image.fromarray(image_array)
    img.save(output_path)

def encrypt_image(image_array):
    # Simple mathematical operation: add a constant value
    key = 50
    encrypted = (image_array + key) % 256  # Ensuring values stay in valid range
    
    # Pixel swapping (for a more complex method)
    height, width, channels = encrypted.shape
    for y in range(height):
        for x in range(0, width, 2):  # Swap pairs of pixels horizontally
            if x + 1 < width:  # Ensure there's a pixel to swap with
                encrypted[y, x], encrypted[y, x + 1] = encrypted[y, x + 1], encrypted[y, x]
    
    return encrypted

def decrypt_image(encrypted_array):
    # Reverse the swapping operation
    height, width, channels = encrypted_array.shape
    for y in range(height):
        for x in range(0, width, 2):
            if x + 1 < width:
                encrypted_array[y, x], encrypted_array[y, x + 1] = encrypted_array[y, x + 1], encrypted_array[y, x]

    # Reverse the mathematical operation
    key = 50
    decrypted = (encrypted_array - key) % 256
    return decrypted

def main():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    input_path = os.path.join(current_dir, 'input_image.png')
    encrypted_path = os.path.join(current_dir, 'encrypted_image.png')
    decrypted_path = os.path.join(current_dir, 'decrypted_image.png')
    
    # Load the image
    image_array = load_image(input_path)
    
    # Encrypt the image
    encrypted_image = encrypt_image(image_array)
    save_image(encrypted_image.astype(np.uint8), encrypted_path)
    
    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image)
    save_image(decrypted_image.astype(np.uint8), decrypted_path)

if __name__ == '__main__':
    main()
