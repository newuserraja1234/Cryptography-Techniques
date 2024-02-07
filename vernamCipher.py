alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,step_length):
    ciphertext =''
    arr1=[]
    arr2=[]
    for letter in plain_text:
        arr1.append(alphabets.index(letter))
    for letter in step_length:
        arr2.append(alphabets.index(letter))
    for i in range(0,len(plain_text)):
        position=arr1[i]+arr2[i]
        if(position>26):
            position=position-26
        ciphertext+=alphabets[position]
    print(f"ciphertext is {ciphertext}")
def decryption(cipher_text,step_length):
    plain_text = ''
    arr1 = []
    arr2 = []
    for letter in cipher_text:
        arr1.append(alphabets.index(letter))
    for letter in step_length:
        arr2.append(alphabets.index(letter))
    for i in range(0, len(cipher_text)):
        position = arr1[i] -arr2[i]
        if (position < 0):
            position = position + 26
        plain_text+= alphabets[position]
    print(f"ciphertext is {plain_text}")
##DRIVER CODE##
while True:
    print("\nEnter 'encrypt' to do encryption and Enter 'decrypt' to do decryption:\n")
    option = input()
    if(option=='encrypt'):
        words=input("\nEnter the sentence/word you want to encrypt:\n ")
        step_length=input("\nEnter the encryption key:\n")
        encryption(plain_text=words,step_length=step_length)

    elif(option=='decrypt'):
        words = input("\nEnter the sentence/word you want to decrypt:\n ")
        step_length = input("\nEnter the decryption key:\n")
        decryption(cipher_text=words, step_length=step_length)

    repeat=input("\nDo you want to do again:(y/n)\n")
    if repeat=='n':
        break
    else:
        continue
