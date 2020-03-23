
def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        ch = text[i]
        # Encrypt uppercase characters in plain text
        if (ch.isupper()):
            result += chr((ord(ch) + s - 65) % 26 + 65)             #ord used to convert char to int
        elif (ch==' '):
            result +=' '
        elif (ch.islower()):
            result += chr((ord(ch) + s - 97) % 26 + 97)             #chr used to convert int to char back
    return result

def decrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        ch = text[i]
        # Encrypt uppercase characters in plain text
        if (ch.isupper()):
            result += chr((ord(ch) - s - 65) % 26 + 65)             #ord used to convert char to int
        elif (ch==' '):
            result +=' '
        elif (ch.islower()):
            result += chr((ord(ch) - s - 97) % 26 + 97)             #chr used to convert int to char back
    return result

def brf(ctext):
    for i in range(26):
        print (i+1, end=' ')
        print(decrypt(ctext,i))

while (1):
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.Brute Force \n 4.EXIT"))
    if choice == 1:
        text = input("Enter plain text: ")
        s = int(input("Enter shift value: "))
        print("Plain Text : " + text)
        print("Shift pattern : " + str(s))
        print("Cipher: " + encrypt(text, s))

    elif choice == 2:

        ctext = input("\nEnter cipher text: ")
        ss = int(input("\nEnter shift value: "))
        print("PlainText: " + decrypt(ctext, ss))
    elif choice ==3:
        ctext = input("\nEnter cipher text: ")
        print("\nBrute forcing\n")
        brf(ctext)

    elif choice == 4:
        exit()
    else:
        print("Choose correct choice")