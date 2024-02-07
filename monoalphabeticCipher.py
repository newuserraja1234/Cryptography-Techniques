alphabets = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a',
    ' ': ' ',
    ',': ',',
    '.': '.',
    '!': '!'
}
list_value = list(alphabets.values())
list_key = list(alphabets.keys())

def find_key(val):
    pos = list_value.index(val)
    key = list_key[pos]
    return key

def encryption(plaintext):
    ciphertext = ''
    for i in plaintext:
        ciphertext += alphabets[i]
    print("The cipher text = ", ciphertext)

def decryption(ciphertext):
    plaintext = ''
    for i in ciphertext:
        key = find_key(i)
        plaintext += key
    print("The plaintext = ", plaintext)


while True:
    user_input = input("Enter 'e' to do encryption and 'd' to do decryption: ")
    if (user_input == 'e'):
        print()
        words = input("Enter the sentence/word you want to encrypt: ")
        encryption(words)

    elif (user_input == 'd'):
        print()
        words = input("Enter the sentence/word you want to decrypt: ")
        decryption(words)

    print()
    repeat = input("Do you want to do again:(y/n) ")
    if repeat == 'n':
        break

