# Tkinter Calculator
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("320x340")
root.minsize(320, 340)
root.maxsize(320, 340)
root.title("Calculator")
# root.wm_iconbitmap("calc1.ico")


def entry(event):
    txt = event.widget.cget('text')

    if txt == '=':
        if inpvar.get().isdigit():
            value = int(inpvar.get())

        else:
            try:
                value = eval(inpvar.get())
            except Exception as e:
                    print(e)
                    value= "ERROR"
                    
        inpvar.set(value)
        inp.update()

    elif txt == 'AC':
        inpvar.set("")
        inp.update()

    elif txt == '%':
        if inpvar.get().isdigit():
            temp = inpvar.get()
            val = int(temp)/100
            inpvar.set(val)
            inp.update()
        else:
            temp = eval(inpvar.get())
            val = int(temp)/100
            inpvar.set(val)
            inp.update()

    elif txt == 'EXIT':
        root.destroy()

    else:
        inpvar.set(inpvar.get()+txt)
        inp.update()

inpvar = StringVar()
inpvar.set("")
inp = Entry(root, textvariable=inpvar, font="lucida 20")
inp.pack(ipady=26,ipadx=90,pady=10,padx=10)


f0 = Frame(root)
btn = Button(f0,text="AC", width=14, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f0,text="%", width=14, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f0,text="EXIT", width=14, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
f0.pack()

f1 = Frame(root)
btn = Button(f1,text="7", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f1,text="8", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f1,text="9", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f1,text="*", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
f1.pack()


f2 = Frame(root)
btn = Button(f2,text="4", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f2,text="5", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f2,text="6", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f2,text="-", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
f2.pack()


f3 = Frame(root)
btn = Button(f3,text="1", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f3,text="2", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f3,text="3", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f3,text="/", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
f3.pack()


f4 = Frame(root)
btn = Button(f4,text=".", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f4,text="0", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f4,text="=", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
btn = Button(f4,text="+", width=10, height=2)
btn.pack(side = LEFT)
btn.bind("<Button-1>", entry)
f4.pack()

root.mainloop()