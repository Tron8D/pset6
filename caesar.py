import sys

if len(sys.argv) != 2:
    sys.exit("Use key: caesar <key>")
    
def encrypt(text, key):
    print("ciphertext:", end=" ")
    for i in range(len(text)):
        if (text[i].islower()):
            c = ord("a") + (ord(text[i]) - ord("a") + key) % 26
            print(chr(c), end="")
        elif (text[i].isupper()):
            c = ord("A") + (ord(text[i]) - ord("A") + key) % 26
            print(chr(c), end="")
        else:
            print(text[i], end="")
    print()
    
key = int(sys.argv[1])
if (key == 0):
    exit(0)
    
text = input("plaintext: ")
encrypt(text, key)
