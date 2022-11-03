while(True):
    print("\n  please select an option")
    print("1 tea......20")
    print("2 coffee......10")
    print("3 burger.......45")
    print("4 sandwich......50")
    print("5 alpham.......100")
    print("6 generate bill")
    print("7 exit")
    ch=int(input("Enter the choice"))
    
    if(ch==1):
        print("Added Tea")
        qty=int(input("enter the quantity"))
        total=20*qty
        l.append("tea x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
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
