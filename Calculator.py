from tkinter import *
import math
π = math.pi
def button_press(num):
	global equation_text
	equation_text= str(equation_text) + str(num)
	equation_label.set(equation_text)

def equals():
	global equation_text
	try:
		total = str(eval(equation_text))
		equation_label.set(total)
		equation_text = total
	except ZeroDivisionError:
		equation_label.set('Arithmetic Error')
		equation_text=''
	except SyntaxError:
		equation_label.set('Syntax Error')
		equation_text=''

def clear():
	global equation_text
	equation_label.set('')
	equation_text =""


def sqroot(t):
	global equation_text
	total3 =(eval(str(equation_text))**t)
	equation_label.set(total3)
	equation_text = total3

		
root = Tk()
root.geometry("350x500")
root.resizable(width=False, height=False)
root.configure(bg='paleturquoise')
root.title('My Calculator!')



equation_text=""
equation_label=StringVar()

label =Label(root, textvariable=equation_label,font='helvetica 20 bold', bg='paleturquoise',fg='black',height=2,width=20,justify=LEFT,anchor='e') 
label.place(anchor=CENTER, relx=0.5, rely=0.315)

def square(p):
	global equation_text
	total2 = str(float(eval(equation_text))**p)[:18]
	equation_label.set(total2)
	equation_text = total2



button1 = Button(root, text="7", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(7))
button1.place(relx=0.01, rely=0.52)
button2 = Button(root, text="8", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(8))
button2.place(relx=0.249, rely=0.52)
button3 = Button(root, text="9", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(9))
button3.place(relx=0.485, rely=0.52)
button4 = Button(root, text="4", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(4))
button4.place(relx=0.01, rely=0.64)
button5 = Button(root, text="5", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(5))
button5.place(relx=0.249, rely=0.64)
button6 = Button(root, text="6", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(6))
button6.place(relx=0.485, rely=0.64)
button7 = Button(root, text="1", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(1))
button7.place(relx=0.01, rely=0.76)
button8 = Button(root, text="2", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(2))
button8.place(relx=0.249, rely=0.76)
button9 = Button(root, text="3", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(3))
button9.place(relx=0.485, rely=0.76)
button0 = Button(root, text="0", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press(0))
button0.place(relx=0.249, rely=0.88)
button_equal = Button(root, text="=", fg='black', bg="skyblue",height=3, width=12,
	command= equals)
button_equal.place(relx=.723, rely=0.88)
buttonpoint = Button(root, text=".", fg='black', bg="lightblue",height=3, width=10,
	command= lambda:button_press('.'))
buttonpoint.place(relx=0.485, rely=0.88)
button_clear= Button(root, text="Clear", fg='black', bg="skyblue",height=3, width=10,
	command= clear)
button_clear.place(relx=0.01, rely=0.88)

buttonplus= Button(root, text="+", fg='black', bg="sandybrown",height=3, width=12,
	command= lambda:button_press('+'))
buttonplus.place(relx=0.723, rely=0.76)

buttonminus= Button(root, text="-", fg='black', bg="sandybrown",height=3, width=12,
	command= lambda:button_press('-'))
buttonminus.place(relx=0.723, rely=0.64)

buttonmult= Button(root, text="x", fg='black', bg="sandybrown",height=3, width=12,
	command= lambda:button_press('*'))
buttonmult.place(relx=0.723, rely=0.52)
buttondiv= Button(root, text="/", fg='black', bg="sandybrown",height=3, width=12,
	command= lambda:button_press('/'))
buttondiv.place(relx=0.723, rely=0.4)

buttonroot= Button(root, text="√", fg='black', bg="sandybrown",height=3, width=10,
	command= lambda:sqroot(0.5))
buttonroot.place(relx=0.01, rely=0.4)
buttonsq= Button(root, text="x²", fg='black', bg="sandybrown",height=3, width=10,
	command=lambda: square(2))
buttonsq.place(relx=0.249, rely=0.4)
buttonpi= Button(root, text="π", fg='black', bg="sandybrown",height=3, width=10,
		command= lambda:button_press('π'))
buttonpi.place(relx=0.485, rely=0.4)

root.mainloop()