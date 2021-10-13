from tkinter import *
#defining functions=====================================================
def btnclk(numbers):
    global operator
    operator= operator+str(numbers)
    text_input.set(operator)

def btncleardisplay():
    global operator
    operator=""
    text_input.set("")    

def btnequalsinput():
     global operator
     total=str(eval(operator))
     text_input.set(total)
     operator=""

mainwindow=Tk()
mainwindow.title("calculator")
operator=""
text_input=StringVar()




   #defining maintext 

maintext=Entry(mainwindow,textvariable=text_input,bd=30,width=12,justify="right",font=('arial',24),bg="powder blue",fg="black").grid(columnspan=40)

#defining buttons

btnzero=Button(mainwindow,padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="0",command=lambda:btnclk(0)).grid(row=4,column=1)


btn7=Button(mainwindow,command=lambda:btnclk(7),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="7").grid(row=1,column=1)
btn8=Button(mainwindow,command=lambda:btnclk(8),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="8").grid(row=1,column=2)
btn9=Button(mainwindow,command=lambda:btnclk(9),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="9").grid(row=1,column=3)

btn4=Button(mainwindow,command=lambda:btnclk(4),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="4").grid(row=2,column=1)
btn5=Button(mainwindow,command=lambda:btnclk(5),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="5").grid(row=2,column=2)
btn6=Button(mainwindow,command=lambda:btnclk(6),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="6").grid(row=2,column=3)


btn1=Button(mainwindow,command=lambda:btnclk(1),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="1").grid(row=3,column=1)
btn2=Button(mainwindow,command=lambda:btnclk(2),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="2").grid(row=3,column=2)
btn3=Button(mainwindow,command=lambda:btnclk(3),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="3").grid(row=3,column=3)

btnaddition=Button(mainwindow,command=lambda:btnclk("+"),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="+").grid(row=1,column=4)
btnsubstraction=Button(mainwindow,command=lambda:btnclk("-"),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="-").grid(row=2,column=4)
btnmultiplication=Button(mainwindow,command=lambda:btnclk("*"),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="*").grid(row=3,column=4)
btndivision=Button(mainwindow,command=lambda:btnclk("/"),padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="/").grid(row=4,column=4)




btnclear=Button(mainwindow,command=btncleardisplay,padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="c").grid(row=4,column=2)
btnequals=Button(mainwindow,command=btnequalsinput,padx=16,pady=8,font=('arial',24),bg="powder blue",fg="black",text="=").grid(row=4,column=3)



































mainwindow.mainloop()