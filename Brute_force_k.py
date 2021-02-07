


cipher =input('Enter the Cipher Text:')

if cipher.isupper():
    LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
else:
    LETTERS='abcdefghijklmnopqrstuvwxyz'

for key in range(len(L)):
    message=''
    for symbol in cipher:
        if symbol in L:
            loc = L.find(symbol)
            loc=loc-key
            if loc <0:
                loc=loc+26
            message=message+L[loc]
        else:
            message=message+symbol
    print('key value: %s Decrypted message: %s'%(key,message))

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:

            translated = translated + symbol

    print('Hacking key %s: %s' % (key, translated))
