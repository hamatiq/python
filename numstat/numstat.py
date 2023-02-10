try:
    file = open("numbers.txt",'r')
except OSError:
    print("File error File numbers.txt dose not exist!")
else:
    try:
        stat = file.read()
    except OSError:
        print("could not read file")
    else:
        stat = stat.strip()
        stat= stat.split('\n')
        stat = list(map(int,stat))
        print ("Sum:" +str(sum(stat)))
        print ("Count:"+ str(len(stat)))
        print ("Average:"+ str(sum(stat)/len(stat)))
        print ("Max:"+str(max(stat)))
        print("Min:" + str(min(stat)))
        print("Range:"+ str(max(stat)-min(stat)))

