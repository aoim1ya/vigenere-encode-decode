import os #Để sử dụng clear screen
apb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(code,key):
    realkey = key 
    encrypted = ''
    vitri = 0
    while len(realkey) < len(code): #Kéo dài độ dài key = độ dài code bằng cách lặp đi lặp lại key
        if vitri < len(key):
            realkey += key[vitri]
            vitri += 1
        else:
            vitri = 0
            realkey += key[vitri]
            vitri += 1
        
    for i in range (len(code)):
        x = apb.index(code[i].lower()) + apb.index(realkey[i].lower()) #Tìm vị trí của kí tự mới với index = index của kí tự trong code + index của kí tự trong key. Nếu index >= 26 thì chạy lại từ đầu danh sách
        if x <= 25:
            encrypted += apb[x]
        else:
            encrypted += apb[x - 26] #(x-26) vì nếu x - 25 thì 26 - 25 == 1 không phải vị trí đầu danh sách
    print('Encrypted text:' , encrypted)
             

def decrypt(cipher,key):
    realkey = key
    decrypted = ''
    vitri = 0
    while len(realkey) < len(cipher):
        if vitri < len(key):
            realkey += key[vitri]
            vitri += 1
        else:
            vitri = 0
            realkey += key[vitri]
            vitri += 1

    for i in range (len(cipher)):
        x = apb.index(cipher[i].lower()) - apb.index(realkey[i].lower()) #Tìm vị trí của kí tự mới với index = index của kí tự trong code - index của kí tự trong key. Nếu index < 0 thì chạy lại từ cuối danh sách
        #if x >= 0:
            #decrypted += apb[x]
        #else:
            #decrypted += apb[x + 26]
        decrypted += apb[x] #If x < 0, it will go back from the bottom of the alphabet
    print('Decrypted text:' , decrypted)

while True:
    os.system('cls')
    mode = int(input('Press 1 to encrypt, press 2 to decrypt: '))
    while mode != 1 and mode != 2: #Các phần while ở dưới lặp đi lặp lại để tránh trường hợp nhập sai. Loop dừng lại khi nhập đúng
        os.system('cls')
        print('Press 1 or 2 again \n')
        mode = int(input('Press 1 to encrypt, press 2 to decrypt: '))

    if mode == 1:
        os.system('cls')
        code = input('Type the text you want to encrypt: ')
        key = input('Type your key: ')

        while code.isalpha() == False or key.isalpha() == False or len(code) < len(key):
            print('All the characters must be alphabetic and the text cannot be shorter than the key. Type again\n')
            code = input('Type the text you want to encrypt:')
            key = input('Type your key:')

        encrypt(code, key)
        exit()

    if mode == 2:
        os.system('cls')
        cipher = input('Type the text you want to decrypt: ')
        key = input('Type your key: ')

        while cipher.isalpha() == False or key.isalpha() == False or len(cipher) < len(key):
            print('All the characters must be alphabetic and the text cannot be shorter than the key. Type again\n')
            cipher = input('Type the text you want to encrypt:')
            key = input('Type your key:')

        decrypt(cipher, key)
        exit()

        
        



