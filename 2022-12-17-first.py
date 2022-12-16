from tkinter import*
import tkinter as tk

ORD = Tk()
ORD.resizable(False, False)
ORD.title("원랜디 룰렛 프로그램")
ORD.geometry("600x1000+200+100")

button = Button(ORD,width=15,height=5, fg="black", bg="white", text='룰 뽑기')
button.pack(padx=60,pady=60)
ORD.mainloop()