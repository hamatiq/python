#in this case we are replacing every charecter with a unique charecter
dictinary = {
    "a":"0",
    "b":"1",
    "c":"2",
    "D":"3",
    "e":"4",
    "f":"5",
    "g":"6",
    "h":"7",
    "i":"8",
    "j":"9",
    "k":"!",
    "l":"@",
    "m":"#",
    "n":"$",
    "o":"%",
    "p":"^",
    "q":"&",
    "r":"*",
    "s":"(",
    "t":")",
    "u":"-",
    "v":"+",
    "w":"<",
    "x":">",
    "y":"?",
    "z":"=",
}
rdict = {}
rdict = dict(zip(dictinary.values(), dictinary.keys()))


def encrypt(msg):
    enmsg=""
    for m in msg:
        if (dictinary.get(m) != None):
            enmsg+=dictinary.get(m)
        else:
            enmsg+=m
    return (enmsg)

def decrypt(msg):
    enmsg=""
    for m in msg:
        if (rdict.get(m) != None):
            enmsg+=rdict.get(m)
        else:
            enmsg+=m

    return (enmsg)

# print (decrypt("7070"))

while (True):
    p = input("Welcome to the Secret Message Encoder/Decoder\n1. Encode a message\n2. Decode a message\n3. Exit\n")

    if ( p == "1" ):
        msg = input("Enter a message to encode: ")
        print (encrypt(msg)+"\n")
        continue
    
    elif (p == "2"):
        msg = input("Enter a message to decode: ")
        msg = str(msg)
        print (decrypt(msg)+"\n")
        continue
    
    elif (p=="3"):
        break

    else:
        print (p+" is not a valid choice. \nPlease enter a number between 1 and 3.\n")
        continue
