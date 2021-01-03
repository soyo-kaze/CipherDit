import cipher

alpha = 0

def encrypto(word,key):
    global alpha
    #word= input("enter: ")
    #key = input("enter: ")
    key2 = cipher.enc(key)
    print(key2)
    key2 = int((str(int(int(key2)/773)))[:2])
    if key2 < 40:
        key2 +=30
    print(key2)
    """*********************encryption***************"""
    lst = []
    for x in word:
        #print(lst,end="\n")
        if x == " ":
            alpha = word.index(x)
        A = 93 - (ord(str(x)) + int(key))
        while A < (-93):
            A = 126 + A
        A += 33 
        if A >= 0:
            lst.append(chr(int(A)))
        elif A < 0:
            lst.append(chr(-(int(A))))
    print(lst[alpha])
    return "".join(lst)

def decrypto(word,key):
    global alpha
    #word= input("enter: ")
    #key = input("enter: ")
    key2 = cipher.enc(key)
    print(key2)
    key2 = int((str(int(int(key2)/773)))[:2])
    if key2 < 40:
        key2 +=30
    print(key2)
    """*********************decryption***************"""
    lst = []
    for x in word:
        #print(lst,end="\n")
        A = 93 + (ord(str(x)) - int(key))
        while A < (-93):
            A = 126 - A
        A += 33 
        if A >= 0:
            lst.append(chr(int(A)))
        elif A < 0:
            lst.append(chr(-(int(A))))
    ppl = "".join(lst)
    n = lst[alpha]
    for x in lst:
        if x == n:
            #print(lst.index(x))
            lst[lst.index(x)] = " "
    ppl = "".join(lst)
    print(alpha)
    return ppl
word = "hwllo how aeeessa"
key = "40"
xello = encrypto(word,key)
print(xello)
print(decrypto(xello,key))
