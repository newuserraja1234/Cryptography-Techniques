alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, step_length):
    cipher_text=''
    for letter in plain_text:
        if letter == ' ' or letter == '?' or letter == '!' or letter == ',' or letter == '.':
            cipher_text += letter
            continue
        else:
            position = alphabets.index(letter)
            new_position = (position + step_length)% 26
            cipher_text += alphabets[new_position]
    print("\n The cipher text is",cipher_text)

def decryption(cipher_text, step_length):
    original_text=""
    for letter in cipher_text:
        if letter == ' ' or letter == '?' or letter == '!' or letter == ',' or letter == '.':
            original_text += letter
            continue
        else:
            position = alphabets.index(letter)
            new_position = (position-step_length) % 26
        if(new_position < 0):
            new_position += 26
        original_text += alphabets[new_position]
    print("\n The plain text is", original_text)

while True:
    print("\nEnter 'encrypt' to do encryption and Enter 'decrypt' to do decryption : ")
    option = input()
    if(option == 'encrypt'):
        words = input("\n Enter the sentences to be encrypted:\n")
        step_length = int(input("\n Enter the encryption key : \n"))
        encryption(plain_text = words, step_length = step_length)

    elif(option == 'decrypt'):
        words = input("\n Enter the encrypted text to be decrypted: \n")
        step_length = int(input("\n Enter the decryption key : \n"))
        decryption(cipher_text = words, step_length = step_length)

    repeat =  input("\n Do you want to do again:(y/n).")
    if repeat == 'n':
        break
    else:
        continue
