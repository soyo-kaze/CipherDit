import cipher


# ----------------------encryption---------------------------

def encrypto(word, key):
    lst = []
    key2 = cipher.enc(key)
    # print(key2)
    key2 = int(str(int(int(key2)/773))[:len(str(int(key2)))-10:-1])
    # print(key2)
    for x in word:
        # print(lst,end="\n")
        A = int(ord(x)) + int(key2)
        while A > 126:
            A -= 126
        lst.append(chr(int(A)))
    prin = "".join(lst)
    return prin
# -----------------------------------------------------------


# ----------------------decryption---------------------------

def decrypto(word, key): 
    lst = []
    key2 = cipher.enc(key)
    key2 = int(str(int(int(key2)/773))[:len(str(int(key2)))-10:-1])
    # print(key2)
    for x in word:
        # print(lst,end="\n")
        A = int(ord(x)) - int(key2)
        while A < 0:
            A += 126
        lst.append(chr(int(A)))
    rin = "".join(lst)
    return rin
# ----------------------------------------------------------
