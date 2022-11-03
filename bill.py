import mysql.connector
import sys
from datetime import datetime
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='hoteldb')
except mysql.connector.Error as e:
    #print("connection error")
    sys.exit("dbconnection failure")   
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
        qty=int(input("enter the quantity"))
        total=50*qty
        l.append("sandwich x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(ch==5):
        print("Added Alpham")
        qty=int(input("enter the quantity"))
        total=100*qty
        l.append("alpham x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(ch==6):
        print("Generating bill")
         
        name = input('Enter the name : ')
        phoneno = input('Enter the phone number : ')
        #dates = input('Enter the date in the form of yyyy-mm-d : ')
        l1 = []
        l1.extend(l)
        count = 0
        for i in l1:
            l.remove(i)
            amount = count
         #print(f'Total amount {count} ')
         try:
             sql = sql="INSERT INTO `billing`( `name`, `phnno`, `amount`, `date`) VALUES (%s,%s,%s,now())"
             data = (name,phoneno,amount)
             mycursor.execute(sql,data)
             mydb.commit()
        except mysql.connector.Error as e:
            sys.exit("insert error")
        print('data inserted ')
    elif(ch==7):
        break
