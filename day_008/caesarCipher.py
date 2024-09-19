alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(encrypt_text, l_shift):
    result = ""
    for i in encrypt_text:
        if(i != ' '):
            index = (alphabet.index(i) + l_shift)
            if(index > 25):
                index = abs((25 - index)) - 1
            result += alphabet[index]
        else:
            result += " "
    print(result)

def decrypt(decrypt_text, l_shift):
    result = ""
    for i in decrypt_text:
        if(i != ' '):
            index = (alphabet.index(i) - l_shift)
            if(index < 0):
                print(f"index: {index}")
                index = 25 - abs(index)
            result += alphabet[index]
        else:
            result += " "
    print(result)

while True:
    direction = input("Type 'enconde' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        exit()


