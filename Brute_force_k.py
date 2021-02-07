def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

text = input("Enter string: ")
s = int(input("Enter shift number: "))
print("Original string: ", text)
plain=encrypt(text,s)
print("After encryption: ", encrypt(text, s))


cipher =input('Enter the Cipher Text:')

if cipher.isupper():
    LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
else:
    LETTERS='abcdefghijklmnopqrstuvwxyz'



for key in range(len(LETTERS)):
    translated = ''
    for symbol in cipher:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:

            translated = translated + symbol

    print('Hacking key %s: %s' % (key, translated))
