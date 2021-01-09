# import modules 

import whois 
from tkinter import *
from tkinter import messagebox 
# user define funtion 
# for get domain information 
def Domain_info():
        messagebox.showinfo("Information","Please Wait..While our software is fetching your information.")
        domain = whois.whois(str(e1.get()))
        server.set(domain.whois_server)
        exp_date.set(domain.expiration_date)
        reg_name.set(domain.name)
        org.set(domain.org)
        state.set(domain.state)
        city.set(domain.city)
        country.set(domain.country) 


# object of tkinter 
# and background set for red 
master = Tk() 
master.configure() 
master.geometry("450x250") 
master.title("Whois Gui Tool")


# Variable Classes in tkinter 
server = StringVar() 
exp_date = StringVar() 
reg_name = StringVar() 
org = StringVar() 
state = StringVar() 
city = StringVar() 
country = StringVar() 

# Creating label for each information 
# name using widget Label 
Label(master, text="Website URL : ").grid(row=0, sticky=W) 
Label(master, text="Server Name :").grid(row=3, sticky=W) 
Label(master, text="Expiration date :").grid(row=4, sticky=W) 
Label(master, text="Registerar name :").grid(row=5, sticky=W) 
Label(master, text="Organisation :").grid(row=6, sticky=W) 
Label(master, text="State :").grid(row=7, sticky=W) 
Label(master, text="City :").grid(row=8, sticky=W) 
Label(master, text="Country :").grid(row=9, sticky=W) 

# Creating lebel for class variable 
# name using widget Entry 
Label(master, text="", textvariable=server).grid(row=3, column=1, sticky=W) 
Label(master, text="", textvariable=exp_date).grid(row=4, column=1, sticky=W) 
Label(master, text="", textvariable=reg_name).grid(row=5, column=1, sticky=W) 
Label(master, text="", textvariable=org).grid(row=6, column=1, sticky=W) 
Label(master, text="", textvariable=state).grid(row=7, column=1, sticky=W) 
Label(master, text="", textvariable=city).grid(row=8, column=1, sticky=W) 
Label(master, text="", textvariable=country).grid(row=9, column=1, sticky=W) 

Label(master, text="A Tool By DMT H4CK3R").grid(row=14, column=1, sticky=W) 


e1 = Entry(master) 
e1.grid(row=0, column=1) 

def quit():
	master.destroy()

# creating a button using the widget 
# Button that will call the submit function 
b = Button(master, text="Submit", command=Domain_info,bd='5') 
b.grid(row=0, column=5) 
b2 = Button(master, text="Exit ", command=quit,bd='5',width='5') 
b2.grid(row=0, column=6) 


mainloop()
