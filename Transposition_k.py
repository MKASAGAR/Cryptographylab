import math
key=input('Enter the key value:')
message=input('Enter the text message:')

key_list=[]

for k in key:
    key_list.append(int(k))

print(key_list)

########

key_len=len(key_list)
msg_len=len(message)

print(key_len)
print(msg_len)

#################

row = math.ceil(msg_len/key_len)

message_matrix=[['x' for i in range(key_len)] for j in range (row)]

print(message_matrix)

##################

i=0
j=0

for m in message:
    if j < key_len:
        message_matrix[i][j]=m
        j=j+1
    else:
        j=0
        i=i+1
        message_matrix[i][j]=m
        j=j+1

print(message_matrix)

#########################3
cipher=[]

for k in range(1,key_len+1):
    column=key_list.index(k)
    for r in range(row):
        cipher.append(message_matrix[r][column])

print(cipher)


cipher_string=''

for ch in cipher:
    cipher_string=cipher_string+ch

print('The cipher Text:')
print(cipher_string)
print('Decryption Message:')
for i in range(math.ceil(msg_len/key_len)):
    for j in range(len(key_list)):
        print(message_matrix[i][j],end='')


