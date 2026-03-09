#!/usr/bin/python

#First of all, listen. I can code, but idk how to code. Now, you can read the code :3

from tkinter import *
import random
import time
import json

#Function called whenever question is selected, and at the beginning :)
def randomize_bg():
    global ran_color
    #the hell is this built-in function
    ran_color=hex(random.randint(0, 4194303))
    win.configure(bg="#"+ran_color[2:].zfill(6))
    question_lbl.config(bg="#"+ran_color[2:].zfill(6))
    validate_lbl.config(bg="#"+ran_color[2:].zfill(6))
    button_frm.config(bg="#"+ran_color[2:].zfill(6))
    answer_frm.config(bg="#"+ran_color[2:].zfill(6))
    validate_btn.config(highlightbackground="#"+ran_color[2:].zfill(6))

#Validate the answer to the question
def validate():
    global current_num
    global current_str
    if answer_ent.get().casefold() == questions[current_num].answer.casefold():
        questions[current_num].completed=True
        validate_str.set("Correct")
        validate_lbl.config(fg="darkgreen")
        validate_btn.config(state="disabled")
        question_btn[current_num].config(bg="#00ff00")
    else:
        validate_str.set("Faux")
        validate_lbl.config(fg="red")

#Change the current question to the selected one
def switch(num):
    global current_str
    global current_num
    current_str.set(questions[num].question_str)
    current_num = num
    validate_str.set("")
    answer_ent.delete(0, END)
    randomize_bg()
    #Enable or disable the validate button
    if questions[current_num].completed == True:
        validate_btn.config(state="disabled")
    else:
        validate_btn.config(state="active")

ran_color=hex(random.randint(0, 16777215))

class Question:
    def __init__(self, question_str, answer, result):
        self.question_str = question_str
        self.answer = answer
        self.result = result
        self.completed = False

#Case insensitive btw :3c
questions = []
with open("questions.json", "r", encoding="utf-8") as file:
        question_data = json.load(file)
        for i in range(len(question_data)):
            questions.append(Question(question_data[i]["question_str"], question_data[i]["answer"], question_data[i]["result"]))

question_btn = [None] * len(questions)

#Create the window
win = Tk()
#Make the win fullscreen
win.attributes("-fullscreen", True)

'''
#Create the window that will contain the progress bar
progress = Tk()
progress.configure(bg="black")
progress.attributes("-fullscreen", True)

#Create the canva for the gradient and the bar
progress_cnv = Canvas(
    progress,
    bg="red"
)
progress_cnv.place(
    relx=0.5,
    rely=0.1,
    relw=0.95,
    relh=0.05,
    anchor=CENTER
)

progress.update()

progress_cnv_w = progress_cnv.winfo_width()
progress_cnv_h = progress_cnv.winfo_height()

print(progress_cnv_w)
print(progress_cnv_h)

progress_rect = [None] * len(question)

list_colors = ["green", "blue", "cyan", "black", "grey", "green", "blue", "cyan", "black", "grey"]

for i in range(len(question)):
    print(int(progress_cnv_w/len(question)))
    progress_rect[i] = progress_cnv.create_rectangle(
        i*int(progress_cnv_w/len(question)),
        0,
        int(progress_cnv_w/len(question)),
        progress_cnv_h-2,
        fill=list_colors[i]
    )
#progress_cnv.create_rectangle(1, 1, int(progress_cnv.winfo_width()/len(question)), progress_cnv.winfo_height()-2, fill="green");
'''
#The current selected question
current_num = 0
current_str = StringVar(win, questions[0].question_str)

valid_img = PhotoImage(file="valid1.png")

#The Correct or Faux string
validate_str = StringVar(win, "")

#Container for all the question selection button
button_frm = Frame(
    win,
    bg="#"+ran_color[2:].zfill(6)
)
button_frm.pack(side=BOTTOM)

#Element that shows the question
question_lbl = Label(
    win,
    textvariable=current_str,
    bg="#"+ran_color[2:].zfill(6),
    font=("Helvetica, 30 bold"),
    anchor="center"
)
question_lbl.pack(
    side=TOP,
    pady=(150, 0)
)

#Element that shows Correct or Faux
validate_lbl = Label(
    win,
    textvariable=validate_str,
    bg="#"+ran_color[2:].zfill(6),
    font=("Arial, 22 italic")
)
validate_lbl.pack(
    side=TOP,
    pady=30
)

#Container for the entry and the validate button
answer_frm = Frame(
    win,
    bg="#"+ran_color[2:].zfill(6)
)
answer_frm.pack(side=TOP)

#You can enter the answer here
answer_ent = Entry(
    answer_frm,
    font=("Arial, 22"),
    justify=CENTER,
    fg="white",
    bg="black",
    highlightthickness=0,
    borderwidth=5,
    insertbackground="grey"
)
answer_ent.pack(
    side=LEFT,
    padx=(40, 0)
)

#Confirm the answer
validate_btn = Button(
    answer_frm,
    #text="Valider",
    image=valid_img,
    font=("Arial, 26"),
    relief="ridge",
    borderwidth=7,
    bg="darkred",
    activebackground="red",
    highlightbackground="#"+ran_color[2:].zfill(6),
    command=validate,
    state="active"
)
validate_btn.pack(
    side=RIGHT,
    pady=20,
    padx=(10, 20)
)

#Generate question selection button
for i in range(len(questions)):
    question_btn[i] = Button(
        button_frm,
        text=str(i+1),
        font=("Arial, 25 bold"),
        bg="darkorange",
        activebackground="yellow",
        command=lambda i=i: switch(i),
        width=3,
        borderwidth=5,
        highlightbackground="black",
        highlightthickness=3
    )
    question_btn[i].pack(
        side=LEFT,
        padx=20,
        pady=(0, 50)
    )

randomize_bg()
            
#The mainloop idk
win.mainloop()
#progress.mainloop()