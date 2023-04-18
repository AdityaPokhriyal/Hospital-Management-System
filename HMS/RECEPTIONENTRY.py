def menu():
    while (c=='y'):
        print ("Press 1 to Add New data")
        print ("Press 2 to Update Existing data")
        print ("Press 3 to Delete data")
        print ("Press 4 to Display data")
        print ("Press 5 to to EXIT")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            adddata()
        elif choice == 2:
            updatedata()
        elif choice == 3:
            deldata()
        elif choice == 4:
            fetchdata()
        elif choice == 5:
            print("")
            break
        else:
            print ("Wrong input")
c = input("Do you want to continue: ")            

def fetchdata():
    import mysql.connector
    try:
        db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='hospital_patients')
        cursor = db.cursor()
        cursor.execute("select * from patients")
        results = cursor.fetchall()
        for x in results:
            print(x)
    except:
        print ("Error: Unable to get information")

def adddata():
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='hospital_patients')
    cursor = db.cursor()
    sql = input("Enter sql insert command for patient table:")
    cursor.execute(sql)
    db.commit()
    print("Data added")
    
def updatedata():
    import mysql.connector
    try:
        db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='hospital_patients')
        cursor = db.cursor()
        sql =input("Enter update command:")
        cursor.execute(sql)
        print("Data updated")
        db.commit()
    except exception as e:
        print(e)
        
def deldata():
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='hospital_patients')
    cursor = db.cursor()
    sql = input("Enter command for a record to be deleted:")
    cursor.execute(sql)
    print("Record deleted")
    db.commit()

menu()    
