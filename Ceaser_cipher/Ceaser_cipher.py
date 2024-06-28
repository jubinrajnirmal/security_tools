def ceaser_encrypt(text,shift):
    encrypted = ""
    for i in text:
        if i.isalpha():
            shift1 = shift % 26
            if i.islower():
                code = ord(i) + shift1
                if code > ord('z'):
                    code -= 26
            elif i.isupper():
                code = ord(i) + shift1
                if code > ord('Z'):
                    code -= 26
            encrypted += chr(code)
        else:
            encrypted += code
    return encrypted


def ceaser_decrypt(text,shift):
    return ceaser_encrypt(text, -shift)

def main ():
    print("----------------------------------------------------------------------------------------------")
    print("Ceaser Cipher Script \n")
    print("!This script only supports aplhabets! \n")
    while True:
        mode = input("Want to (E)ncrypt or (D)ecrypt your text? ").upper()
        if mode in [ 'E' , 'D']:
            break
        else:
            print("Please enter right choice, *E* for encryption and *D* for decryption")    
    input_message = input('Enter your text --> ')
    shift_value = int(input('Enter the shift value --> '))

    if mode == 'E':
        encrypt_msg = ceaser_encrypt(input_message, shift_value)
        print(f"Encrypted text --> {encrypt_msg} ")
    if mode == 'D':
        decrypt_msg = ceaser_decrypt(input_message, shift_value)
        print(f"Decrypted text --> {decrypt_msg} ")
    print("---------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()


