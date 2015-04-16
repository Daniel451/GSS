
import hashlib
import re
import time

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha384 = hashlib.sha384()
sha512 = hashlib.sha512()

csalt = "xohth4dew5p8"
chash = "199f066a0bac4140e792d1d4a434ae44"


dic = open("german.dic", "r")


found = False


start = time.time()

for line in dic:
    # read line and strip line
    word = line.strip()
    # check if word is longer than 5 or contains uppercase
    if(len(word) > 5 or re.search("[A-Z]", word)):
        continue
    if(chash == hashlib.md5(csalt+word).hexdigest()):
        ende = time.time()
        print("found the password in " + str(ende-start)  + "s!\n" + "it is: " + word)
        found = True
        break

if not found:
    print("did not found the password :(")
