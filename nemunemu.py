import random

def nemunemu():
    chrord = random.randint(128000, 128063)
    str1 = "ねむねむにゃんこだにゃん"
    str2 = chr(chrord)
    str3 = str1 + str2
    print(str3)