from tkinter import *

root = Tk()

root.title("Calculator")
root.geometry("280x380")
root.resizable(0,0)
root.config(bg= "black")

result_label = Label(root, text=0, bg = "black", fg = "white")
result_label.grid(row=0,column=0,pady=(50,25))
result_label.config(font=("verdana", 30, "bold"))

#1
one_btn = Button(root, text=1, bg = "#05c3f3", fg = "white",width=5, height=2)
one_btn.grid(row=1,column=0)
one_btn.config(font=("verdana", 14))
#2
two_btn = Button(root, text=2, bg = "#05c3f3", fg = "white",width=5, height=2)
two_btn.grid(row=1,column=1)
two_btn.config(font=("verdana", 14))
#3
three_btn = Button(root, text=3, bg = "#05c3f3", fg = "white",width=5, height=2)
three_btn.grid(row=1,column=2)
three_btn.config(font=("verdana", 14))
#4
four_btn = Button(root, text=4, bg = "#05c3f3", fg = "white",width=5, height=2)
four_btn.grid(row=2,column=0)
four_btn.config(font=("verdana", 14))
#5
five_btn = Button(root, text=5, bg = "#05c3f3", fg = "white",width=5, height=2)
five_btn.grid(row=2,column=1)
five_btn.config(font=("verdana", 14))
#6
six_btn = Button(root, text=6, bg = "#05c3f3", fg = "white",width=5, height=2)
six_btn.grid(row=2,column=2)
six_btn.config(font=("verdana", 14))
#7
seven_btn = Button(root, text=7, bg = "#05c3f3", fg = "white",width=5, height=2)
seven_btn.grid(row=3,column=0)
seven_btn.config(font=("verdana", 14))
#8
eight_btn = Button(root, text=8, bg = "#05c3f3", fg = "white",width=5, height=2)
eight_btn.grid(row=3,column=1)
eight_btn.config(font=("verdana", 14))
#9
nine_btn = Button(root, text=9, bg = "#05c3f3", fg = "white",width=5, height=2)
nine_btn.grid(row=3,column=2)
nine_btn.config(font=("verdana", 14))
#0
zero_btn = Button(root, text=0, bg = "#05c3f3", fg = "white",width=5, height=2)
zero_btn.grid(row=4,column=1)
zero_btn.config(font=("verdana", 14))
  

###Operators###
#clear
five_btn = Button(root, text="C", bg = "#05c3f3", fg = "white",width=5, height=2)
five_btn.grid(row=4,column=0)
five_btn.config(font=("verdana", 14))
#.
six_btn = Button(root, text=".", bg = "#05c3f3", fg = "white",width=5, height=2)
six_btn.grid(row=4,column=2)
six_btn.config(font=("verdana", 14))
#+
seven_btn = Button(root, text="+", bg = "#05c3f3", fg = "white",width=5, height=2)
seven_btn.grid(row=1,column=3)
seven_btn.config(font=("verdana", 14))
#-
eight_btn = Button(root, text="-", bg = "#05c3f3", fg = "white",width=5, height=2)
eight_btn.grid(row=2,column=3)
eight_btn.config(font=("verdana", 14))
#*
nine_btn = Button(root, text="*", bg = "#05c3f3", fg = "white",width=5, height=2)
nine_btn.grid(row=3,column=3)
nine_btn.config(font=("verdana", 14))
#/
zero_btn = Button(root, text="/", bg = "#05c3f3", fg = "white",width=5, height=2)
zero_btn.grid(row=4,column=3)
zero_btn.config(font=("verdana", 14))
  

root.mainloop()