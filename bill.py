while(True):
    print("\n  please select an option")
    print("1 tea")
    print("2 coffee")
    print("3 burger")
    print("4 sandwich")
    print("5 alpham")
    print("6 generate bill")
    print("7 exit")
    ch=int(input("Enter the choice"))
    
    if(ch==1):
        print("Added Tea")
    elif(ch==2):
        print("Added Coffee")
    elif(ch==3):
        print("Added Burger")
    elif(ch==4):
        print("Added Sandwich")
    elif(ch==5):
        print("Added Alpham")
    elif(ch==6):
        print("Generating bill")
    elif(ch==7):
        break
