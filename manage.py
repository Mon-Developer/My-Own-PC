from tkinter import *
import os



root=Tk()

#root.geometry('950x600+50+30')
#root.title('Movie Descriptions')
#root.resizable('True','False')


root.title("Manage computer All in place")
root.config(bg='gray20')
titleImage=PhotoImage(file="images\settings.png")

titleLabel=Label(root,text="  computer Manager",font=('elephant',24,'bold'),fg='gold2',bg='gray20',image=titleImage,
                 compound=LEFT)
titleLabel.grid()
frame=Frame(root,bd=8,relief='groove')
frame.grid(row=1)


#Task Manage

taskImage=PhotoImage(file="images\search.png")
Button(frame,text="  Task Manager",font=('arial',15,'bold'),image=taskImage,compound=LEFT,fg='red4',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('taskmgr')).grid(padx=10,sticky='w',pady=10) 

 

 #Control Panel

controlImage=PhotoImage(file="images\search.png")
Button(frame,text="  control Panel",font=('arial',15,'bold'),image=controlImage,compound=LEFT,fg='red3',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('Control')).grid(row=0,column=1,padx=10,sticky='w',pady=10) 
 

 #Date & Time


datetimeImage=PhotoImage(file="images\search.png")
Button(frame,text="  Date & Time",font=('arial',15,'bold'),image=datetimeImage,compound=LEFT,fg='red3',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('timedate.cpl')).grid(row=1,column=0,padx=10,sticky='w',pady=10)


#System Services

servicesImage=PhotoImage(file="images\search.png")
Button(frame,text=" System Services",font=('arial',15,'bold'),image=servicesImage,compound=LEFT,fg='maroon',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('services.msc')).grid(row=1,column=1,padx=10,sticky='w',pady=10) 



#Device Manager

deviceImage=PhotoImage(file="images\search.png")
Button(frame,text="  Device Manager",font=('arial',15,'bold'),image=deviceImage,compound=LEFT,fg='red3',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('devmgmt.msc')).grid(row=2,column=0,padx=10,sticky='w',pady=10) 



#Windows Update

windowImage=PhotoImage(file="images\search.png")
Button(frame,text=" Windows Update",font=('arial',15,'bold'),image=windowImage,compound=LEFT,fg='red3',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('control Update')).grid(row=2,column=1,padx=10,sticky='w',pady=10) 



#Mouse Properties

mouseImage=PhotoImage(file="images\search.png")
Button(frame,text="  Mouse Properties",font=('arial',15,'bold'),image=mouseImage,compound=LEFT,fg='red3',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('main.cpl')).grid(row=3,column=0,padx=10,sticky='w',pady=10) 



#System Properties

propertiesImage=PhotoImage(file="images\search.png")
Button(frame,text="  System Properties",font=('arial',15,'bold'),image=propertiesImage,compound=LEFT,fg='red3',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('sysdm.cpl')).grid(row=3,column=1,padx=10,sticky='w',pady=10) 



#Uninstall Softwares

softwareImage=PhotoImage(file="images\search.png")
Button(frame,text="  Uninstall Software",font=('arial',15,'bold'),image=softwareImage,compound=LEFT,fg='red3',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('appwiz.cpl')).grid(row=4,column=0,padx=10,sticky='w',pady=10) 



#Networking Connections

networkingImage=PhotoImage(file="images\search.png")
Button(frame,text="  Network Connections",font=('arial',15,'bold'),image=networkingImage,compound=LEFT,fg='red3',bg='whitesmoke'
       ,cursor='hand2',bd=0,command=lambda :os.system('ncpa.cpl')).grid(row=4,column=1,padx=10,sticky='w',pady=10) 







root.mainloop()