from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnclearDisplay():
    global operator
    operator = ''
    text_input.set('')

def total():
    global operator
    try:
        result = str(eval(operator))
        text_input.set(result)
        operator = result
    except Exception as a:
        text_input.set('error: '+str(a))
        operator = ''
def absu():
    global operator
    text_input.set(abs(float(text_input.get())))
    operator = str(abs(float(text_input.get())))

ca = Tk()
ca.title('Calculator')
cal = Canvas(ca, bg='#121212')
operator = ''
text_input = StringVar()

txtDisplay = Entry(cal, textvariable=text_input, font=('arial', 50, 'bold'), insertwidth=4,
                   bg='#121212', fg='#0f0', justify='right').grid(columnspan=4, ipadx=20)

btn7 = Button(cal, text='7', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(7), relief=FLAT, highlightcolor='gray').grid(row=1, column=0)
btn8 = Button(cal, text='8', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(8), relief=FLAT).grid(row=1, column=1)
btn9 = Button(cal, text='9', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(9), relief=FLAT).grid(row=1, column=2)
add = Button(cal, text='+', font=('arial', 20, 'bold'), fg='green',
             bg='#121212', width=4, pady=16, command=lambda: btnClick('+'), relief=FLAT).grid(row=2, column=3)

btn4 = Button(cal, text='4', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(4), relief=FLAT).grid(row=2, column=0)
btn5 = Button(cal, text='5', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(5), relief=FLAT).grid(row=2, column=1)
btn6 = Button(cal, text='6', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(6), relief=FLAT).grid(row=2, column=2)
sub = Button(cal, text='_', font=('arial', 20, 'bold'), fg='green',
             bg='#121212', width=4, pady=16, command=lambda: btnClick('-'), relief=FLAT).grid(row=3, column=3)

btn1 = Button(cal, text='1', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(1), relief=FLAT).grid(row=3, column=0)
btn2 = Button(cal, text='2', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(2), relief=FLAT).grid(row=3, column=1)
btn3 = Button(cal, text='3', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(3), relief=FLAT).grid(row=3, column=2)
mul = Button(cal, text='x', font=('arial', 20, 'bold'), fg='green',
             bg='#121212', width=4, pady=16, command=lambda: btnClick('*'), relief=FLAT).grid(row=4, column=3)

btn0 = Button(cal, text='0', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(0), relief=FLAT).grid(row=4, column=0)
btndot = Button(cal, text='.', font=('arial', 20, 'bold'), fg='green',
                bg='#121212', width=4, pady=16, command=lambda: btnClick('.'), relief=FLAT).grid(row=4, column=1)
btnequal = Button(cal, text='=', font=('arial', 20, 'bold'), fg='green',
                  bg='#121212', width=4, pady=16,command=total, relief=FLAT).grid(row=4, column=2)
div = Button(cal, text='/', font=('arial', 20, 'bold'), fg='green',
             bg='#121212', width=4, pady=16, command=lambda: btnClick('/'), relief=FLAT).grid(row=5, column=3)
btnclear = Button(cal, text='C', font=('arial', 20, 'bold'), fg='green',
                  bg='#121212', width=4, pady=16, command=lambda: btnclearDisplay(), relief=FLAT).grid(row=1, column=3)
btnx = Button(cal, text='(', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick('('), relief=FLAT).grid(row=5, column=0)
btny = Button(cal, text=')', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=lambda: btnClick(')'), relief=FLAT).grid(row=5, column=1)
btnabs = Button(cal, text='abs()', font=('arial', 20, 'bold'), fg='green',
              bg='#121212', width=4, pady=16, command=absu, relief=FLAT).grid(row=5, column=2)


cal.pack(fill=BOTH, expand=1)
cal.mainloop()
