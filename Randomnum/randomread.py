try:
    file = open("randomnum.txt","r")
except OSError:
    print("File error File randomnum.txt dose not exist!")
else:
    print(file.read())