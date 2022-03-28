from msilib.schema import Error
from tkinter import*
from tkinter import messagebox
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("MCC Library Login System")
        self.root.geometry("1000x664+100+50")
        self.root.resizable(False,False)
        #displaying background
        self.bg=PhotoImage(file="C:\python\image.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #login panel 
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500 )
        title=Label(Frame_login,text="Login Here",font=("Rockwell Extra Bold",30,"bold")).place(x=100,y=20)
        std=Label(Frame_login,text="MCC Student's Library Login Area",font=("Goudy old style",15,"bold")).place(x=100,y=80)
        username=Label(Frame_login,text="Username",font=("Goudy old style",14,"bold"),fg="Black").place(x=100,y=120)
        self.txt_user=Entry(Frame_login,font=('time new roman',14),bg=("lightgrey"))
        self.txt_user.place(x=100,y=150,height=30,width=330)
        password=Label(Frame_login,text="Password",font=("Goudy old style",14,"bold"),fg="Black").place(x=100,y=180)
        self.txt_pass=Entry(Frame_login,font=('time new roman',14),bg=("lightgrey"))
        self.txt_pass.place(x=100,y=210,height=30,width=330)  
        #button section
        forget=Button(Frame_login,command=self.forget_func,text="forget password ?",bg="white",fg="red").place(x=100,y=240)
        login_Button=Button(self.root ,command=self.login_func,text=" LOGIN ",font=("bold"),bg="lightgrey",fg="Black").place(x=500,y=430)
    def login_func(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","Enter the Username or Password",parent=self.root)
        elif self.txt_user.get()!="210915"or self.txt_pass.get()!="shubham559":
            messagebox.showerror("Error","Entered Username or Password is Wrong",parent=self.root) 
        else:
            messagebox.showinfo("welcome",f"welcome {self.txt_user.get()}\nyour password: {self.txt_pass.get()}\n now you can acces to the library",parent=self.root)
    def forget_func(self):
        messagebox.showinfo("ForgetPassword","Now You Can Change the password ",parent=self.root)
root=Tk()
obj=login(root)
root.mainloop()