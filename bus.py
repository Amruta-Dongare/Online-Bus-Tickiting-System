from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import width
import pymysql


class ConnectorDB: 

    def __init__(self,root):
        self.root=root
        titlespace=" "
        self.root.title(102*titlespace+"MYSQL Connector")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width=False, height=False)
        # =============================== Grid section======================================================
        MainFrame = Frame(self.root, bd=10,width=770, height=700,relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()


        TitleFrame = Frame(MainFrame, bd=7,width=770, height=100,relief = RIDGE)
        TitleFrame.grid(row = 0, column =0 )
        TopFrame3 = Frame(MainFrame , bd=5,width=770, height=500,relief = RIDGE)
        TopFrame3.grid(row= 1 , column = 0)


        LeftFrame = Frame(TopFrame3, bd=5,width=770, height=400, padx=2, bg= "Cadet blue",relief = RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame , bd=5,width=600, height=180,padx=2, pady=4,relief = RIDGE)
        LeftFrame1.pack(side=TOP,padx=0,pady=0)
        

        RightFrame1 = Frame(TopFrame3, bd=5,width=100, height=400, padx=2, bg= "Cadet blue",relief = RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1 , bd=5,width=90, height=300,padx=2, pady=2,relief = RIDGE)
        RightFrame1a.pack(side=TOP)
        # ===================================== variables =============================================================
        
        BusNo=StringVar()
        BusName=StringVar()
        Start=StringVar()
        Stop=StringVar()
        Departure=StringVar()
        Arrival=StringVar()
        

         # ============================================Functions for the manipulation======================================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("MYSQL Connection","Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return
        def Reset():
            self.entBusNo.delete(0,END)
            self.entBusName.delete(0,END)
            self.entStart.delete(0,END)
            self.entStop.delete(0,END)
            self.entDeparture.delete(0,END)
            self.entArrival.delete(0,END)
            
        def addData():
            if BusNo.get()== "" or BusName.get()=="" or Start.get()=="" or Stop.get()=="" or Departure.get()=="" or Arrival.get()=="":
                tkinter.messagebox.showerror("MYSql Connection","Enter correct Details")
            else:
                sqlCon= pymysql.connect(host="localhost",user="root",password="Amruta@2206",database="bus_tickting_system")
                cur=sqlCon.cursor()
                cur.execute("Insert into bus_tickting_system values(%s,%s,%s,%s,%s,%s)",(BusNo.get(),BusName.get(),Start.get(),Stop.get(),Departure.get(),Arrival.get()))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")

        def DisplayData():
            sqlCon= pymysql.connect(host="localhost",user="root",password="Amruta@2206",database="bus_tickting_system")
            cur=sqlCon.cursor()
            cur.execute("select * from bus_tickting_system")
            result=cur.fetchall()
            if len(result) !=0:
                self.bus.delete(*self.bus.get_children())
                for row in result:
                    self.bus.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Displayed Successfully")
            
            
        def TraineeInfo(ev):
            viewInfo = self.bus.focus()
            learnerData = self.bus.item(viewInfo)
            row = learnerData['values']
            BusNo.set(row[0]),BusName.set(row[1]),Start.set(row[2]),Stop.set(row[3]),Departure.set(row[4]),Arrival.set(row[5])

        def update():
            sqlCon= pymysql.connect(host="localhost",user="root",password="Amruta@2206",database="bus_tickting_system")
            cur=sqlCon.cursor()
            cur.execute("update bus_tickting_system set BusName=%s,Start=%s,Stop=%s,Depature=%s,Arrival=%s where BusNo= %s",(BusName.get(),Start.get(),Stop.get(),Departure.get(),Arrival.get(),BusNo.get()))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")
        
        def delete():
            sqlCon= pymysql.connect(host="localhost",user="root",password="Amruta@2206",database="bus_tickting_system")
            cur=sqlCon.cursor()
            cur.execute("delete from bus_tickting_system where BusNo= %s",BusNo.get())
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Deleted Successfully")
            Reset()

        def searchdb():
            try:
                sqlCon= pymysql.connect(host="localhost",user="root",password="Amruta@2206",database="bus_tickting_system")
                cur=sqlCon.cursor()
                cur.execute("select * from bus_tickting_system where Bus_No= %s",BusNo.get())
                row=cur.fetchall()

                BusNo.set(row[0]),BusName.set(row[1]),Start.set(row[2]),Stop.set(row[3]),Departure.set(row[4]),Arrival.set(row[5])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form","NO Such Record Found")
                Reset()
            sqlCon.close()
            

        # ==================================================================================================
        self.lbltitle=Label(TitleFrame,font=('arial',40, 'bold'),text="Bus Tickiting System",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=132)
         # ====================================== label title and buttons============================================================
        self.lblBusNo=Label(LeftFrame1,font=('arial',12, 'bold'),text="Bus No",bd=7)
        self.lblBusNo.grid(row=0,column=0,sticky=W,padx=5)
        self.entBusNo=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=BusNo)
        self.entBusNo.grid(row=0,column=1,sticky=W,padx=5)
        
        self.lblBusName=Label(LeftFrame1,font=('arial',12, 'bold'),text="Bus Name",bd=7)
        self.lblBusName.grid(row=1,column=0,sticky=W,padx=5)
        self.entBusName=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=BusName)
        self.entBusName.grid(row=1,column=1,sticky=W,padx=5)

        self.lblStart=Label(LeftFrame1,font=('arial',12, 'bold'),text="Start",bd=7)
        self.lblStart.grid(row=2,column=0,sticky=W,padx=5)
        self.entStart=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=Start)
        self.entStart.grid(row=2,column=1,sticky=W,padx=5)

        self.lblStop=Label(LeftFrame1,font=('arial',12, 'bold'),text="Stop",bd=7)
        self.lblStop.grid(row=3,column=0,sticky=W,padx=5)
        self.entStop=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=Stop)
        self.entStop.grid(row=3,column=1,sticky=W,padx=5)
        
        self.lblDeparture=Label(LeftFrame1,font=('arial',12, 'bold'),text="Departure",bd=7)
        self.lblDeparture.grid(row=4,column=0,sticky=W,padx=5)
        self.entDeparture=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=Departure)
        self.entDeparture.grid(row=4,column=1,sticky=W,padx=5)

        self.lblArrival=Label(LeftFrame1,font=('arial',12, 'bold'),text="Arrival",bd=7)
        self.lblArrival.grid(row=5,column=0,sticky=W,padx=5)
        self.entArrival=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=Arrival)
        self.entArrival.grid(row=5,column=1,sticky=W,padx=5)

        
        # ==========================================Table TreeView===================================================
        scroll_y=Scrollbar(LeftFrame,orient=VERTICAL)

        self.bus=ttk.Treeview(LeftFrame,height=12,columns=("Bus_No","Bus_Name","Start","Stop","Departure","Arrival"), yscrollcommand= scroll_y.set)
        
        scroll_y.pack(side= RIGHT,fill=Y)

        self.bus.heading("Bus_No",text="BusNo")
        self.bus.heading("Bus_Name",text="BusName")
        self.bus.heading("Start",text="Start")
        self.bus.heading("Stop",text="Stop")
        self.bus.heading("Departure",text="Departure")
        self.bus.heading("Arrival",text="Arrival")
        
        
        self.bus['show']='headings'

        self.bus.column("Bus_No", width=20)
        self.bus.column("Bus_Name", width=40)
        self.bus.column("Start", width=40)
        self.bus.column("Stop", width=60)
        self.bus.column("Departure", width=50)
        self.bus.column("Arrival", width=30)
       
        
        self.bus.pack(fill=BOTH,expand=1)
        self.bus.bind("<ButtonRelease-1>",TraineeInfo)
        


        # =================================================Button function and its coomand ============================================
        self.btnAddNew=Button(RightFrame1a,font=('arial',16, 'bold'),text="Add New",bd=4,pady=1,padx=24,width=8,height=2,command=addData).grid(row=0,column=0,padx=1)

        self.btnDisplay=Button(RightFrame1a,font=('arial',16, 'bold'),text="Display",bd=4,pady=1,padx=24,width=8,height=2,command=DisplayData).grid(row=1,column=0,padx=1)

        self.btnUpdate=Button(RightFrame1a,font=('arial',16, 'bold'),text="Update",bd=4,pady=1,padx=24,width=8,height=2,command=update).grid(row=2,column=0,padx=1)

        self.btnDelete=Button(RightFrame1a,font=('arial',16, 'bold'),text="Delete",bd=4,pady=1,padx=24,width=8,height=2,command=delete).grid(row=3,column=0,padx=1)

        self.btnSearch=Button(RightFrame1a,font=('arial',16, 'bold'),text="Search",bd=4,pady=1,padx=24,width=8,height=2,command=searchdb).grid(row=4,column=0,padx=1)

        self.btnReset=Button(RightFrame1a,font=('arial',16, 'bold'),text="Reset",bd=4,pady=1,padx=24,width=8,height=2,command=Reset).grid(row=5,column=0,padx=1)

        self.btnExit=Button(RightFrame1a,font=('arial',16, 'bold'),text="Exit",bd=4,pady=1,padx=24,width=8,height=2,command=iExit).grid(row=6,column=0,padx=1)
        # ===============================================End of the mainloop==============================================
        
if __name__=='__main__':
    root=Tk()
    application=ConnectorDB(root)
    root.mainloop()