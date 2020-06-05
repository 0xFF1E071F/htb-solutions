with open("./ciphertext") as f:
    data = f.read()

def decrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in reversed(key):
        for i in reversed(range(len(msg))):
            if i == 0:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[-1]))
            else:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[i-1]))
            while tmp < 0:
                tmp += 256
            msg[i] = chr(tmp)

    return ''.join(msg)


letters = "abcdefghijklmnopqrstuvwxyz"
#letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in letters:
    for i in range(21):
        print "{0} {1}".format(char, i)
        print decrypt(char*i, data)