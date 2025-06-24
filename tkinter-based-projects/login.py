from tkinter import * 
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == "shabazekhan768@gmail.com" and password == "1234":
        messagebox.showinfo("yay!","Login Successful")
    else:
        messagebox.showerror("Error", "Wrong email or password")

root = Tk()

root.title("Login Page")
#root.iconbitmap("icons8-flipkart-32.ico")
root.minsize(400,400)

root.configure(background="#03ACFA")

img = Image.open("tkinter/flipkart-logo.png")
resized_img = img.resize((70,70))
new_img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image = new_img)

img_label.pack(pady=(10,10))

text_label = Label(root, text= "Flipkart", fg="white",bg="#03ACFA")
text_label.pack()
text_label.config(font=("verdana",24))

email_label = Label(root, text= "Email", fg="white",bg="#03ACFA")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",14))

email_input = Entry(root, width= 50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root, text= "Password", fg="white",bg="#03ACFA")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",14))

password_input = Entry(root, width= 50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root, text="Login Here", bg="#03ACFA", fg= "black",width= 20, height=2, command= handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))

root.mainloop()