
calculate = True
while(calculate):
    while (True):
        try:
            x0 = float(input("x0:"))
        except ValueError:
            print("numbers only")
        else:
            break
        
    while (True):
        try:
            v0 = float(input("v0:"))
        except ValueError:
            print("numbers only")
        else:
            break

    while (True):
        try:
            a = float(input("a:"))
        except ValueError:
            print("numbers only")
        else:
            break

    while (True):
        try:
            t = float(input("t:"))
            if (t < 0):
                print("time must be >= 0")
                continue
        except ValueError:
            print("numbers only")
        else:
            break

    # Calculate xfx
    xfx= float(x0)+(float(v0)*float(t))+(0.5*float(a)*float(t)* float(t))

    # output
    print('\n xfx:'+ str(xfx))

    # another try?
    calculate = input("another try (y/n):")
    if (calculate != "y"):
        calculate = False
    
