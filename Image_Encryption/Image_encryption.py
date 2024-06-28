from PIL import Image 
import numpy as np 
from math import gcd
import random

def load_image(image_path):
    return Image.open(image_path)

def show_image(image):
    image.show()

def image_to_array(image):
    return np.array(image)

def array_to_image(image_array):
    return Image.fromarray(np.uint8(image_array))

def encrypt_image(image_array, key):
    return (image_array + key) % 256
    
def decrypt_image(image_array, key):
    return (image_array - key) % 256

def swap_pixels(image_array):
    swapped_array = image_array.copy()
    height, width, _ = swapped_array.shape
    for i in range(height):
        for j in range(0, width-1, 2):
            swapped_array[i, j], swapped_array[i, j+1] = swapped_array[i, j+1], swapped_array[i, j]
    return swapped_array

def unswap_pixels(swapped_array):
    unswapped_array = swapped_array.copy()
    height, width, _ = unswapped_array.shape
    for i in range(height):
        for j in range(0, width - 1, 2):
            unswapped_array[i, j], unswapped_array[i, j + 1] = unswapped_array[i, j + 1], unswapped_array[i, j]
    return unswapped_array

if __name__ == "__main__":
    #Input Here 
    image_path = input("Enter the path of the image: ")

    #Prompt for Method and Encryption/ Decryption
    method = input("Choose the method: (1) Math Operation or (2) Swapping pixels " )
    operation = input("Choose the operation: (1) Encryption or (2) Decryption ")

    if method == '1':
        if operation == '1':
            key = int(input('Enter the Key for encryption (int value): '))
            image = load_image(image_path)    
            image_array = image_to_array(image)
            encrypted_array = encrypt_image(image_array, key)
            encrypted_image = array_to_image(encrypted_array)
            encrypted_image.show()
            encrypted_image.save('encrypted_math.jpg')
            print("Successfully encrypted the Image")
        elif operation == '2':
            key = int(input('Enter the Key for encryption (int value): '))
            image = load_image(image_path)    
            image_array = image_to_array(image)
            decrypted_array = decrypt_image(image_array, key)
            decrypted_image = array_to_image(decrypted_array)
            decrypted_image.show()
            decrypted_image.save('decrypted_math.jpg')
            print("Successfully decrypted the Image")
        else:
            print("Incorrect choice of operation, please choose (1) or (2) ")
    
    elif method == "2":
        image = load_image(image_path)
        image_array = image_to_array(image)
        if operation == '1':
            swapped_array = swap_pixels(image_array)
            swapped_image = array_to_image(swapped_array)
            swapped_image.show()
            swapped_image.save('swapped.jpg')
            print("Successfully swapped the pixels of the Image")
        elif operation == '2':
            swapped_image = image
            swapped_array = image_to_array(swapped_image)
            unswapped_array = unswap_pixels(swapped_array)
            unswapped_image = array_to_image(unswapped_array)
            unswapped_image.show()
            unswapped_image.save('unswapped.jpg')
            print('Successfully unswapped the pixels of the Image')
        else:
            print('Incorrect choice of oepration, please choose (1) or (2) ')
    
    else:
        print("Incorrect choice of methode, please choose (1) or (2) ")