from tkinter import *
from tkinter import messagebox
# import whole packages from the tkinter



# Openning the screen
root = Tk()
root.geometry('350x690')
root.minsize(350, 690)
root.maxsize(350, 690)

# Our calculator title
root.title("Simnple calculator")






# We can say the input type for what user operand wen can see all the things in the input field or the Entry
e = Entry(root, width=25, borderwidth=3, font=20)
e.grid(row=0, column=0, columnspan=3, padx=30, pady=50)



ans = 0
def add_number(number):
    global ans
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    print(str(current))
    print(str(number))
    ans = e.get()
    
# Add the numbers
def add_numbers(operators):
    global f_num, know_o
    # if(know_o == '')
    if operators=="+":
        know_o = "+"
        f_num = e.get()
        e.delete(0, END)

    elif operators=="*":
        know_o = "*"
        f_num = e.get()
        e.delete(0, END)    

    elif operators=="/":
        know_o = "/"
        f_num = e.get()
        e.delete(0, END)    

    elif operators=="-":
        know_o = "-"
        f_num = e.get()
        e.delete(0, END)    
    

# To clear the Entry
def button_clear():
    e.delete(0, END)



# Clear one by one
def clear_oneby_one():
    get = e.get()
    le = len(get)
    e.delete(le-1)




# Show the final answer
def ans():
 try:
    s_number = e.get()
    if(s_number  == ''):
        messagebox.showinfo('info', 'Pleased type Somethings')
        return
    print(s_number, 'This is')
    e.delete(0, END)
    if know_o=="+":
       e.insert(0,  int(f_num) + int(s_number) )
    if know_o == '-':
       e.insert(0,   int(f_num)-int(s_number))
    if know_o == '/':
       
       f = int(int(f_num)/int(s_number))
       e.insert(0,  f)    
    if know_o == '*':
       e.insert(0, int(f_num)*int(s_number))   
    else:
        return   
    
 except Exception as h:
    print(h, 'this')
    messagebox.showinfo('info', 'Pleased provide another number.')
    print('ans')



# making the Buttons
button_1 = Button(root, text=1, padx=40, pady=40, command=lambda: add_number(1))
button_2 = Button(root, text=2, padx=40, pady=40, command=lambda: add_number(2))
button_3 = Button(root, text=3, padx=40, pady=40, command=lambda: add_number(3))
button_4 = Button(root, text=4, padx=40, pady=40, command=lambda: add_number(4))
button_5 = Button(root, text=5, padx=40, pady=40, command=lambda: add_number(5))
button_6 = Button(root, text=6, padx=40, pady=40, command=lambda: add_number(6))
button_7 = Button(root, text=7, padx=40, pady=40, command=lambda: add_number(7))
button_8 = Button(root, text=8, padx=40, pady=40, command=lambda: add_number(8))
button_9 = Button(root, text=9, padx=40, pady=40, command=lambda: add_number(9))
button_0 = Button(root, text=0, padx=40, pady=40, command=lambda: add_number(0))

button_add = Button(root, text='+', padx=40, pady=40, command=lambda: add_numbers("+"))
button_multi = Button(root, text="*", padx=40, pady=40, command=lambda: add_numbers("*"))
button_div = Button(root, text="/", padx=40, pady=40, command=lambda: add_numbers("/"))
button_difference = Button(root, text="-", padx=40, pady=40, command=lambda: add_numbers("-"))

button_cls = Button(root, text="Clear", bg="red", fg="white",padx=33, pady=33, command=button_clear)
clear_one_by_one  = Button(root, text="OC", bg="red", fg="white", padx=33, pady=33, command=clear_oneby_one)


# This is for the final answers
equal_button = Button(root, text='=', command=ans, padx=40, pady=40, bg="black", fg='white')






# Put the button on the screen
button_1.grid(row=5, column=2)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=2, column=0)
button_6.grid(row=2, column=1)
button_7.grid(row=2, column=2)
button_8.grid(row=2, column=0)
button_9.grid(row=3, column=1)
button_0.grid(row=3, column=1)
button_add.grid(row=3, column=2)
equal_button.grid(row=3, column=0)
button_cls.grid(row=4, column=0)
clear_one_by_one.grid(row=4, column=1)
button_multi.grid(row=4, column=2)
button_difference.grid(row=5, column=0)
button_div.grid(row=5, column=1)

# Handels the infinite request for the Events
root.mainloop()