from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Square Calculator")
root.geometry("700x200+400+100")
root.resizable(False, False)

def sqr():
	try:
		s = entNumber.get()
		n = float(s)
		r = n * n
		msg = "square =" + str(r)
		showinfo("Answer", msg)
	except ValueError:
		showerror("Issue", "inavlid input")
		entNumber.delete(0, END)
		entNumber.focus()

lblNumber = Label(root, text="enter a number", font=('courier', 18, 'bold'))
lblNumber.place(x=10, y=50)

entNumber = Entry(root, bd=5, font=('courier', 18, 'bold'))
entNumber.place(x=250, y=50)

btnFind = Button(root, text="find", font=('courier', 18, 'bold'), command=sqr)
btnFind.place(x=250, y=100)

root.mainloop()


	