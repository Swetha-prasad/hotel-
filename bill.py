import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='hoteldb')
mycursor = mydb.cursor()
total=0
item=[]
l=[]
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
        item.append("tea x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(ch==2):
        print("Added Coffee")
        qty=int(input("enter the quantity"))
        total=10*qty
        item.append("coffee x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(ch==3):
        print("Added Burger")
        print("burger added")
        qty=int(input("enter the quantity"))
        total=45*qty
        l.append("burger x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(ch==4):
        print("Added Sandwich")
    elif(ch==5):
        print("Added Alpham")
    elif(ch==6):
        print("Generating bill")
    elif(ch==7):
        break
