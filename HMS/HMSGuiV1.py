from tkinter import *
from tkinter.ttk import *
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='HospitalAV')
cursor = db.cursor()

win = Tk()
win.title("Hospital Manegement System")
win.geometry("300x200")

#FUNCTION FOR ADDING DATA
def adddata(event):
    win1 = Tk()
    #PATIENT ID
    l = Label(win1,text="Enter Patient ID: ")
    patientID = Entry(win1)
    l.grid(row=1,column=1,sticky=W)
    patientID.grid(row=1,column=2)
    
    #NAME ENTRY
    l2 = Label(win1,text="Enter Patient Name: ")
    name = Entry(win1)
    l2.grid(row=2,column=1,sticky=W)
    name.grid(row=2,column=2)
 
    #AGE ENTRY
    l3 = Label(win1,text="Enter Age:")
    age = Entry(win1)
    l3.grid(row=3,column=1,sticky=W)
    age.grid(row=3,column=2)
   
    #DISEASE ENTRY
    l4 = Label(win1,text="Enter Disease or Illness:")
    disease_illness = Entry(win1)
    l4.grid(row=4,column=1,sticky=W)
    disease_illness.grid(row=4,column=2)
   
    #DOCTOR NAME
    l5 = Label(win1,text="Enter Doctor Name:")
    doctorname = Entry(win1)
    l5.grid(row=5,column=1,sticky=W)
    doctorname.grid(row=5,column=2)
   
    #PHONE NUMBER
    l6 = Label(win1,text="Enter your Phone Number:")
    phonenumber = Entry(win1)
    l6.grid(row=6,column=1,sticky=W)
    phonenumber.grid(row=6,column=2)
    
    #ADDRESS
    l7 = Label(win1,text="Enter your Address:")
    address = Entry(win1)
    l7.grid(row=7,column=1,sticky=W)
    address.grid(row=7,column=2)

    a = patientID
    b = name
    c = age
    d = disease_illness
    e = doctorname
    f = phonenumber
    g = address

    global qry
    qry = "INSERT INTO patients VALUES(%s,%s,%s,%s,%s,%s,%s)"
    global data
    data = (a,b,c,d,e,f,g)
   
    def click():
        
        global a
        a = patientID.get()
        global b
        b = name.get()
        global c
        c = age.get()
        global d
        d = disease_illness.get()
        global e
        e = doctorname.get()
        global f
        f = phonenumber.get()
        global g
        g = address.get()
        print(a,b,c,d,e,f,g)

        cursor.execute("insert into patients values("+'"'+a+'"'+','+'"'+b+'"'+','+ str(c) +','+'"'+d+'"'+','+'"'+e+'"'+','+'"'+f+'"'+','+'"'+g+'"'+')')    
        db.commit()
        
    #ENTER BUTTON 
    b1 =  Button(win1,text="Enter",command=click)
    b1.grid(row=8,column=1)
      
    win1.mainloop()

#FUNCTION TO UPDATE DATA
def updatedata(event):
    win1 = Tk()
    #PATIENT ID
    l = Label(win1,text="Enter Patient ID: ")
    patientID = Entry(win1)
    l.grid(row=1,column=1,sticky=W)
    patientID.grid(row=1,column=2)
    
    #NAME ENTRY
    l2 = Label(win1,text="Enter Patient Name: ")
    name = Entry(win1)
    l2.grid(row=2,column=1,sticky=W)
    name.grid(row=2,column=2)
 
    #AGE ENTRY
    l3 = Label(win1,text="Enter Age:")
    age = Entry(win1)
    l3.grid(row=3,column=1,sticky=W)
    age.grid(row=3,column=2)
   
    #DISEASE ENTRY
    l4 = Label(win1,text="Enter Disease or Illness:")
    disease_illness = Entry(win1)
    l4.grid(row=4,column=1,sticky=W)
    disease_illness.grid(row=4,column=2)
   
    #DOCTOR NAME
    l5 = Label(win1,text="Enter Doctor Name:")
    doctorname = Entry(win1)
    l5.grid(row=5,column=1,sticky=W)
    doctorname.grid(row=5,column=2)
   
    #PHONE NUMBER
    l6 = Label(win1,text="Enter your Phone Number:")
    phonenumber = Entry(win1)
    l6.grid(row=6,column=1,sticky=W)
    phonenumber.grid(row=6,column=2)
    
    #ADDRESS
    l7 = Label(win1,text="Enter your Address:")
    address = Entry(win1)
    l7.grid(row=7,column=1,sticky=W)
    address.grid(row=7,column=2)

    def click1():

        global a
        a = patientID.get()
        global b
        b = name.get()
        global c
        c = age.get()
        global d
        d = disease_illness.get()
        global e
        e = doctorname.get()
        global f
        f = phonenumber.get()
        global g
        g = address.get()
        print(a,b,c,d,e,f,g)
    
        import mysql.connector
        try:
            db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='HospitalAV')
            cursor = db.cursor()
            sql =input("Enter update command:")
            cursor.execute(sql)
            print("Data updated")
            db.commit()

        except exception as exc:
            print(exc)

#FUNCTION TO DELETE DATA        
def deldata(event):
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='HospitalAV')
    cursor = db.cursor()
    sql = input("Enter command for a record to be deleted:")
    cursor.execute(sql)
    print("Record deleted")
    db.commit()    

win.iconbitmap(r"C:\Program Files\AV\HMSicons(.ico)\HMS.ico")

photo1 = PhotoImage(file=r"C:\Program Files\AV\HMSicons(.png)\NEW.png").subsample(20,20)
addnew = Button(win,text="Add New",image=photo1,compound=TOP)
addnew.grid(row=10,column=0,sticky=W,columnspan=1)
addnew.bind("<Button-1>",adddata)

photo2 = PhotoImage(file=r"C:\Program Files\AV\HMSicons(.png)\SAVE.png").subsample(20,20)
save = Button(win,text="Save",image=photo2,compound=TOP)
save.grid(row=10,column=1,sticky=W,columnspan=1)

photo3 = PhotoImage(file=r"C:\Program Files\AV\HMSicons(.png)\UPDATE.png").subsample(20,20)
update = Button(win,text="Update",image=photo3,compound=TOP)
update.grid(row=10,column=3,sticky=W)
update.bind("<Button-1>",updatedata)

photo4 = PhotoImage(file=r"C:\Program Files\AV\HMSicons(.png)\DELETE.png").subsample(20,20)
delete = Button(win,text="Delete",image=photo4,compound=TOP)
delete.grid(row=10,column=5,sticky=W)
delete.bind("<Button-1>",deldata)

win.after(30000,win.destroy)

win.mainloop()
