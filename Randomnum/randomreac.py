import random

#main function 
def randGen(high,low,count):
    random.seed()
    #open file randomnum.txt and over write it or create file randomnum.txt if it dosenot exists
    file = open("randomnum.txt","w") 
    # forloop for a set number n (count)
    for x in range(count):
        file.write(str(random.randrange(low,high))+"\n") #writing to file
    file.close()#closing file

#input validation
while (True):
    try:
        randcount = int(input("How many random numbers do you want:"))
        if(randcount <= 0):
            print("amount of numbers must be grater than 0!")
            continue
    except ValueError:
        print("Whole numbers only!") 
    else:
        break
while (True):
    try:
        randLowBound = int(input("What is the lowest random number should be:"))
    except ValueError:
        print("Whole numbers only!")
    else:
        break
while (True):
    try:
        randHighBound = int(input("What is the highest random number should be:"))
        if(randHighBound<= randLowBound):
            print("Highest number must be grater than lowest number!")
            continue
    except ValueError:
        print("Whole numbers only!")
    else:
        break

#function error validation 
try:
    randGen(randHighBound,randLowBound,randcount)
except:
    print ("problem")
else:
    print("The random numbers were written to randomnum.txt")
