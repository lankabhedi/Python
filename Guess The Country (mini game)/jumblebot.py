import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

answers = ["INDIA", "AMERICA", "AUSTRALIA", "OMAN", "FRANCE"]
questions = []

for i in answers:
    words = list(i)
    shuffle(words)
    questions.append(words)

num = random.randint(0, len(questions)-1)

def initial():
    global questions, num
    lb1.configure(text = questions[num])

def answercheck():
    global questions, num, answers
    userinput = e1.get()
    if userinput.lower() == answers[num].lower():
        messagebox.showinfo("YEEHAW!", "It is correct!")
        num = random.randint(0, len(questions)-1)
        lb1.configure(text = questions[num])
        e1.delete(0, END)
    else:
        messagebox.showinfo("OH DANG!", "Try again!")
        e1.delete(0, END)

def resetswitch():
    global answers, questions, num
    num = random.randint(0, len(questions)-1)
    lb1.configure(text = questions[num])
    e1.delete(0, END)

window = Tk()
window.geometry("300x340")
window.configure(background = "#FBC02D")
window.title("Guess the Country!")
window.iconbitmap("icons8-jake-48.ico")
window.resizable(0, 0)

lb1 = Label(window, font = "times 20", bg = "#FBC02D", fg = "#000000")
lb1.pack(pady = 30, ipady = 10, ipadx = 10)

answer = StringVar()
e1 = Entry(window, textvariable = answer)
e1.pack(ipady = 5, ipadx = 5)

button1 = Button(window, text = "Check", width = 20, command = answercheck, fg = "#000000", bg = "#FFA000")
button1.pack(pady = 40)

button2 = Button(window, text = "Reset", width = 20, command = resetswitch, fg = "#000000", bg = "#FFA000")
button2.pack()

initial()

window.mainloop()