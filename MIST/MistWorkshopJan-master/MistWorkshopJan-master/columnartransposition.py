def encrypt(text,ss):
    c= len(ss)
    ll=len(text)
    r=int(ll/c)+1
    k = 0
    h=0
    if (r * c < ll):
        r = c
    a=[]
    b=[]
    s = [["" for j in range(c)]
         for i in range(r)]

    for i in range(c):
        a.append(ss[i])

    a.sort()
    for i in range(c):
        for j in range(c):
            if(a[i]==ss[j]):
                b.append(j)

    for i in range(r):
        for j in range(c):

            if k >= ll:
                s[i][j] = " "
                k += 1

            else:
                s[i][j] = text[k]
                k += 1



    for j in range(c):
        for i in range(r):
            if s[i][b[j]] == " ":
                break

            print(s[i][b[j]], end="")
            h+=1
            if(h==c-1):
                print(" ",end="")
                h=0



def remove(string):
    return string.replace(" ", "")


while (1):
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if choice == 1:
        text = input("Enter plain text: ")
        text=remove(text)
        s = input("Enter key: ")
        s=remove(s)
        print("Plain Text : " + text)
        print("key : " + str(s))
        # print("Cipher: " + encrypt(text, s))
        encrypt(text,s)
    elif choice == 2:

        ctext = input("\nEnter cipher text: ")
        ss = input("Enter key: ")
        # print("PlainText: " + decrypt(ctext, ss))

    elif choice == 3:
        exit()
    else:
        print("Choose correct choice")
