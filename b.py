import tkinter
from tkinter import filedialog, messagebox
import a

window = tkinter.Tk()
window.title("Write and read file")
window.geometry("600x600+50+50")
window.resizable(False, False)
def openfile():
    filedirection = filedialog.askopenfilename()
    data = a.readfile(filedirection)
    return data
btn1 = tkinter.Button(window, text="Open file", command= openfile).place(x=300, y=400)
box = tkinter.Text(window, font="arial, 10", width=82, height=10).place(x=10, y=100)
box.insert(tkinter.END, openfile)

window.mainloop()