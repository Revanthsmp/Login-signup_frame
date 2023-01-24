import tkinter
from tkinter import *
import tkinter.messagebox
import ast

#creating a screen layout
root = tkinter.Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.config(bg="white")
root.resizable(False,False)

#function for signin button
def signin():
    email = entry_email.get()
    password = entry_password.get()

    file = open("datasheet.txt","r")
    read_file = file.read()
    d = ast.literal_eval(read_file)
    file.close()

    if email == "Email" and  password == "Password":
        tkinter.messagebox.showerror(title="Error",message="All fields are mandatory")

    elif email not in d.keys():
        tkinter.messagebox.showerror(title="Warning",message= "Email does not exist. \n Please sign up if not registered.")

    elif email in d.keys() and password == d[email] :
        screen = Toplevel(root)
        screen.title("Admin")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        tkinter.Label(screen,text="Welcome ! ! !",bg="white",fg="black",font=["times new roman",18,"bold"]).pack(expand=True)

        screen.mainloop()

    elif email in d.keys() and password != d[email] :
        tkinter.messagebox.showerror("Invalid","Invalid Password for the entered Email")

    
def signup_command():
    tab = Toplevel(root)
    tab.title("Sign Up")
    tab.geometry("925x500+300+200")
    tab.config(bg="white")
    tab.resizable(False,False)

    def signup():
        fname=entry_fname.get()
        lname = entry_lname.get()
        email = entry_email.get()
        password = entry_password.get()
        conpass = entry_conpassword.get()

        if fname == "" or lname == "" or email == "" or password == "" or conpass == "" :
            tkinter.messagebox.showerror(title="Error",message="All fields are mandatory")
        
        elif password == conpass :
            try:
                file = open("datasheet.txt","r+")
                read_file = file.read()
                r = ast.literal_eval(read_file)

                dict1 = {email : password}
                r.update(dict1)
                file.truncate()
                file.close()

                file = open("datasheet.txt","w")
                write_file = file.write(str(r))
                file.close()

                tkinter.messagebox.showinfo(title="Congratulations",message="Successfully signed up!")

            except:
                file = open("datasheet.txt","w")
                inputs = str({"email":"pass1"})
                file.write(inputs)
                file.close()

        else:
            tkinter.messagebox.showerror(title="Error",message="Password does not match")
                

    
    def signup_close():
        tab.destroy()

    img = tkinter.PhotoImage(file="C:\Program Files\Python39\Project images\signup.png")
    insert_img = tkinter.Label(tab,image=img,bg="white")
    insert_img.place(x=50,y=70)

    label_signup = tkinter.Label(tab,text="Sign Up",bg="white",fg="blue",font =["times new roman",24,"bold"])
    label_signup.place(x=575,y = 20)

    widget_frame = tkinter.Frame(tab,bg="white",width = 350,height =400)
    widget_frame.place(x=480,y=60)

    #firstname
    def on_entry(e):
        entry_fname.delete(0,"end")

    def on_leave(l):
        fname = entry_fname.get()
        if fname == "":
            entry_fname.insert(0,"Enter Firstname")

    entry_fname = tkinter.Entry(widget_frame,bg="white",fg="black",font=["calibri",12],border=0,width=200)
    entry_fname.place(x=20,y=20)
    entry_fname.insert(0,"Enter Firstname")
    entry_fname.bind("<FocusIn>",on_entry)
    entry_fname.bind("<FocusOut>",on_leave)

    tkinter.Frame(widget_frame,bg="black",height=2,width=300).place(x=15,y =45)

    #lastname
    def on_entry(e):
        entry_lname.delete(0,"end")

    def on_leave(l):
        fname = entry_lname.get()
        if fname == "":
            entry_lname.insert(0,"Enter Lastname")

    entry_lname = tkinter.Entry(widget_frame,bg="white",fg="black",font=["calibri",12],border=0,width=200)
    entry_lname.place(x= 20,y = 75)
    entry_lname.insert(0,"Enter Lastname")
    entry_lname.bind("<FocusIn>",on_entry)
    entry_lname.bind("<FocusOut>",on_leave)

    tkinter.Frame(widget_frame,bg="black",height=2,width=300).place(x=15,y =100)

    #email
    def on_entry(e):
        entry_email.delete(0,"end")

    def on_leave(l):
        fname = entry_email.get()
        if fname == "":
            entry_email.insert(0,"Enter Email")

    entry_email = tkinter.Entry(widget_frame,bg="white",fg="black",font=["calibri",12],border=0,width=200)
    entry_email.place(x= 20,y = 130)
    entry_email.insert(0,"Enter Email")
    entry_email.bind("<FocusIn>",on_entry)
    entry_email.bind("<FocusOut>",on_leave)

    tkinter.Frame(widget_frame,bg="black",height=2,width=300).place(x=15,y =155)

    #password
    def on_entry(e):
        entry_password.delete(0,"end")

    def on_leave(l):
        fname = entry_password.get()
        if fname == "":
            entry_password.insert(0,"Enter Password")

    entry_password = tkinter.Entry(widget_frame,bg="white",fg="black",font=["calibri",12],border=0,width=200)
    entry_password.place(x= 20,y = 185)
    entry_password.insert(0,"Enter Password")
    entry_password.bind("<FocusIn>",on_entry)
    entry_password.bind("<FocusOut>",on_leave)

    tkinter.Frame(widget_frame,bg="black",height=2,width=300).place(x=15,y =210)

    #confirm password
    def on_entry(e):
        entry_conpassword.delete(0,"end")

    def on_leave(l):
        fname = entry_conpassword.get()
        if fname == "":
            entry_conpassword.insert(0,"Re-Enter Password")

    entry_conpassword = tkinter.Entry(widget_frame,bg="white",fg="black",font=["calibri",12],border=0,width=200)
    entry_conpassword.place(x= 20,y =240 )
    entry_conpassword.insert(0,"Re-Enter Password")
    entry_conpassword.bind("<FocusIn>",on_entry)
    entry_conpassword.bind("<FocusOut>",on_leave)

    tkinter.Frame(widget_frame,bg="black",height=2,width=300).place(x=15,y =265)

    #signup button
    button_signup = tkinter.Button(widget_frame,text="Sign up",command=signup,bg="blue",fg="white",pady=7,width=25,font=["times new roman",15,"bold"],activebackground="green",border=0)
    button_signup.place(x=25,y=290,width=280,height=27)

    #button for redirecting to signin
    label_exist = tkinter.Label(tab,text="Already Registered? ",bg="white",fg="black",font=["times new roman",12,"italic"])
    label_exist.place(x=75,y= 360)
    button_signin_redirect = tkinter.Button(tab,text="Sign In",command=signup_close,bg="white",fg="blue",font=["times new roman",15,"underline"],cursor="hand2",border=0,activebackground="green")
    button_signin_redirect.place(x= 210,y=355)



    tab.mainloop()

    
#inserting a img in the screen
img = PhotoImage(file="C:\Program Files\Python39\Project images\login.png")
insert_img = tkinter.Label(root,image=img,bg="white")
insert_img.place(x=50,y=50)

#creating a frame inside the screen to insert labels and entry widgets
widgets_frame = tkinter.Frame(root,bg="white",width=350,height=350)
widgets_frame.place(x=480,y=50)

#sign label
label_signin = tkinter.Label(widgets_frame,text ="Sign In",bg="white",fg="Blue",font=["Times new roman",24,"bold"])
label_signin.place(x= 100,y = 5)

#username entry field
def on_enter(e):
    entry_email.delete(0,"end")

def on_leave(e):
    name = entry_email.get()
    if name =="":
        entry_email.insert(0,"Username")

entry_email = tkinter.Entry(widgets_frame,bg="white",fg="black",border=0,font=["calibri",12])
entry_email.place(x=30,y=80)
entry_email.insert(0,"Email")
entry_email.bind("<FocusIn>",on_enter) #to delete the text "username" on clicking for user-friendly interface 
entry_email.bind("<FocusOut>",on_leave) #restore the text "username" if left empty

#to draw a line below the username entry field
Frame(widgets_frame,bg="black",height=2,width=300).place(x=25,y =107)

#Password entry field
def on_enter(e):
    entry_password.delete(0,"end")

def on_leave(e):
    name = entry_password.get()
    if name =="":
        entry_password.insert(0,"Password")

entry_password = tkinter.Entry(widgets_frame,bg="white",fg="black",border=0,font=["calibri",12])
entry_password.place(x=30,y=150)
entry_password.insert(0,"Password")
entry_password.bind("<FocusIn>",on_enter) #to delete the text "Password" on clicking for user-friendly interface
entry_password.bind("<FocusOut>",on_leave) #restore the text "Password" if left empty

#to draw a line below the password entry field
Frame(widgets_frame,bg="black",height=2,width=300).place(x=25,y =177)

#signin button
button_signin = tkinter.Button(widgets_frame,text="Sign in",command=signin,width=30,pady=7,bg="blue",fg="white",border=0,font=["times new roman",12,"bold"],activebackground="green")
button_signin.place(x=35 ,y =205)

#label and button for signup
label_signup = tkinter.Label(widgets_frame,text="New user?",bg="white",fg="black",font =["calibri",10])
label_signup.place(x=80,y=275)
button_signup = tkinter.Button(widgets_frame,text="Sign up",command=signup_command,bg="white",fg="blue",width=6,border=0,cursor="hand2",font=["times new roman",12],activebackground="green")
button_signup.place(x=140,y=270)


root.mainloop()
