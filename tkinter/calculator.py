from tkinter import *

first_num = second_num = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text = new)

def get_operator(op):
    global first_num, operator
    first_num = int(result_label["text"])
    operator = op
    result_label.config(text="")

def get_result():
    global first_num, second_num,operator

    second_num =int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_num+second_num))

    elif operator == '-':
        result_label.config(text=str(first_num-second_num))

    elif operator == 'x':
        result_label.config(text=str(first_num*second_num))

    else:
        if second_num == 0:
            result_label.config(text="Error")

        else: 
            result_label.config(text=str(round(first_num/second_num,2)))

def clear():
    result_label.config(text='')

root = Tk()

root.title("Calculator")
root.geometry("280x380")
root.resizable(0,0)
root.config(bg= "black")

result_label = Label(root, text="", bg = "black", fg = "white")
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=("verdana", 30, "bold"))

#1
one_btn = Button(root, text=1, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(1))
one_btn.grid(row=1,column=0)
one_btn.config(font=("verdana", 14))
#2
two_btn = Button(root, text=2, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(2))
two_btn.grid(row=1,column=1)
two_btn.config(font=("verdana", 14))
#3
three_btn = Button(root, text=3, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(3))
three_btn.grid(row=1,column=2)
three_btn.config(font=("verdana", 14))
#4
four_btn = Button(root, text=4, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(4))
four_btn.grid(row=2,column=0)
four_btn.config(font=("verdana", 14))
#5
five_btn = Button(root, text=5, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(5))
five_btn.grid(row=2,column=1)
five_btn.config(font=("verdana", 14))
#6
six_btn = Button(root, text=6, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(6))
six_btn.grid(row=2,column=2)
six_btn.config(font=("verdana", 14))
#7
seven_btn = Button(root, text=7, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(7))
seven_btn.grid(row=3,column=0)
seven_btn.config(font=("verdana", 14))
#8
eight_btn = Button(root, text=8, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(8))
eight_btn.grid(row=3,column=1)
eight_btn.config(font=("verdana", 14))
#9
nine_btn = Button(root, text=9, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(9))
nine_btn.grid(row=3,column=2)
nine_btn.config(font=("verdana", 14))
#0
zero_btn = Button(root, text=0, bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_digit(0))
zero_btn.grid(row=4,column=1)
zero_btn.config(font=("verdana", 14))
  

###Operators###
#clear
clr_btn = Button(root, text="C", bg = "#05c3f3", fg = "white",width=5, height=2,command=clear)
clr_btn.grid(row=4,column=0)
clr_btn.config(font=("verdana", 14))
#=
equal_btn = Button(root, text="=", bg = "#05c3f3", fg = "white",width=5, height=2,command=get_result)
equal_btn.grid(row=4,column=2)
equal_btn.config(font=("verdana", 14))
#+
plus_btn = Button(root, text="+", bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_operator('+'))
plus_btn.grid(row=1,column=3)
plus_btn.config(font=("verdana", 14))
#-
sub_btn = Button(root, text="-", bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_operator('-'))
sub_btn.grid(row=2,column=3)
sub_btn.config(font=("verdana", 14))
#*
mul_btn = Button(root, text="x", bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_operator('x'))
mul_btn.grid(row=3,column=3)
mul_btn.config(font=("verdana", 14))
#/
div_btn = Button(root, text="/", bg = "#05c3f3", fg = "white",width=5, height=2,command=lambda:get_operator('/'))
div_btn.grid(row=4,column=3)
div_btn.config(font=("verdana", 14))
  

root.mainloop()