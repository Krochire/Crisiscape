#!/usr/bin/python

#First of all, listen. I can code, but idk how to code. Now, you can read the code :3

from tkinter import *
import random
import json
import sys

#Functions
#=========

#Function called whenever question is selected, and at the beginning :)
def randomize_bg():
    #the hell is this built-in function
    ran_color=hex(random.randint(0, 4194303))
    background_color = "#" + ran_color[2:].zfill(6)
    win.configure(bg=background_color)
    question_lbl.config(bg=background_color)
    validate_lbl.config(bg=background_color)
    button_frm.config(bg=background_color)
    answer_frm.config(bg=background_color)
    validate_btn.config(highlightbackground=background_color)
    result_lbl.config(bg=background_color)

#Validate the answer to the question
def validate():
    global current_num
    global current_str
    global completed_questions
    if answer_ent.get().casefold() == questions[current_num]["answer"].casefold():
        questions[current_num]["completed"]=True
        result_lbl.config(text=questions[current_num]["result"])
        validate_str.set("Correct")
        validate_lbl.config(fg="darkgreen")
        validate_btn.config(state="disabled")
        question_btn[current_num].config(bg="#00ff00")
        completed_questions += 1
        progress_update()
    else:
        validate_str.set("Faux")
        validate_lbl.config(fg="red")

#Change the current question to the selected one
def switch(num):
    global current_str
    global current_num
    current_str.set(questions[num]["question_str"])
    question_btn[current_num].config(state="normal")
    question_btn[current_num].config(relief=RAISED)
    current_num = num
    question_btn[current_num].config(state="disabled")
    question_btn[current_num].config(relief=SUNKEN)
    validate_str.set("")
    answer_ent.delete(0, END)
    randomize_bg()
    #Enable or disable the validate button and the result label
    if questions[current_num]["completed"]:
        validate_btn.config(state="disabled")
        result_lbl.config(text=questions[current_num]["result"])
    else:
        validate_btn.config(state="normal")
        result_lbl.config(text="")

def progress_update():
    ratio = completed_questions / len(questions)
    progress_bar.coords(progress_meter, start_rectangle, (PROGRESS_W * ratio, PROGRESS_H))
    completion_str.set(f"{completed_questions}/{len(questions)}")

#Console gui
#===========
#Case-insensitive btw :3c

#Check if the questions.json exist, otherwise the console is closed
try:
    with open("questions.json", "r", encoding="utf-8") as file:
        question_data = json.load(file)
except FileNotFoundError:
    RED = "\033[0;31m"
    RESET = "\033[0m"
    sys.exit(f"\n{RED}questions.json does not exist, please create it with question_maker.py!{RESET}\n") #\033 are ANSI code colour, [0;31m is red, and [0m is reset

questions = [
    {
        "question_str": question["question_str"],
        "answer": question["answer"],
        "result": question["result"],
        "completed": False,
    }
    for question in question_data
]

#Create the window
win = Tk()
#Make the win fullscreen
win.attributes("-fullscreen", True)

#The current selected question
current_num = 0
current_str = StringVar(win, questions[current_num]["question_str"])

valid_img = PhotoImage(file="valid.png")

#The Correct or Faux string
validate_str = StringVar(win, "")

#Container for all the question selection button
button_frm = Frame(win)
button_frm.pack(side=BOTTOM)

#Element that shows the question
question_lbl = Label(
    win,
    textvariable=current_str,
    font="Helvetica, 30 bold",
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
    font="Arial, 22 italic"
)
validate_lbl.pack(
    side=TOP,
    pady=30
)

#Container for the entry and the validate button
answer_frm = Frame(win)
answer_frm.pack(side=TOP)

#You can enter the answer here
answer_ent = Entry(
    answer_frm,
    font="Arial, 22",
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
    image=valid_img,
    font="Arial, 26",
    relief="ridge",
    borderwidth=7,
    bg="darkred",
    activebackground="red",
    command=validate,
    state="normal"
)
validate_btn.pack(
    side=RIGHT,
    pady=20,
    padx=(10, 20)
)

#Label for the question result
result_lbl = Label(
    win,
    text="",
    font="Helvetica, 24 italic",
    anchor="center"
)
result_lbl.pack()

#Generate question selection button
question_btn = []
for i in range(len(questions)):
    question_btn.append(Button(
        button_frm,
        text=str(i+1),
        font="Arial, 25 bold",
        bg="darkorange",
        relief=RAISED,
        activebackground="yellow",
        command=lambda i=i: switch(i),
        width=3,
        borderwidth=5,
        highlightbackground="black",
        highlightthickness=3
    ))
    question_btn[i].pack(
        side=LEFT,
        padx=20,
        pady=(0, 50)
    )

#Progress bar gui
#================
PROGRESS_W = 1000
PROGRESS_H = 100
completed_questions = 0
start_rectangle = (0, 0)

progress = Tk()
progress.title("Progress Bar")
progress.geometry("1280x720")
progress.configure(bg="#ff9bff")

progress_bar = Canvas(
    progress,
    width=PROGRESS_W,
    height=PROGRESS_H,
    bg="white"
)
progress_bar.pack(
    side=BOTTOM,
    expand=True,
    fill=NONE,
)
progress_meter = progress_bar.create_rectangle( # TODO: Some refactoring here and below because it's duplicate code from progress_update()
    start_rectangle,
    (0, PROGRESS_H),
    fill="darkgreen"
)

completion_str = StringVar(progress, f"{completed_questions}/{len(questions)}")

completion_lbl = Label(
    progress,
    textvariable=completion_str,
    font="Helvetica, 30 bold",
    bg="#ff9bff"
)
completion_lbl.pack(
    side=BOTTOM,
    pady=10
)

switch(0)
#The mainloop idk
win.mainloop()
progress.mainloop()
