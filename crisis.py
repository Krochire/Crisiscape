#!/usr/bin/python

#First of all, listen. I can code, but idk how to code. Now, you can read the code :3

from tkinter import *
import random
import json

class App(Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", True)
        self.questions = self._load_questions()
        self.current_num = 0                                             #Selects the first question by default
        self.current_str = StringVar(self, self.questions[0]["question_str"]) #
        self.validate_str = StringVar(self, "") #This string holds the value used by validate_lbl
        self._build_ui()
        self.randomize_bg()

    def _load_questions(self):
        with open("questions.json", "r", encoding="utf-8") as file:
            question_data = json.load(file)
            #Case-insensitive btw :3c
            return [
                {
                "question_str": q["question_str"],
                "answer": q["answer"],
                "result": q["result"],
                "completed": False,
                }
              for q in question_data
            ]

    def _build_ui(self):
        self._build_question_select()
        self._build_question_labels()
        self._build_answer_widget()

        
    def _build_question_select(self):
        self.button_frm = Frame(self)
        self.button_frm.pack(side=BOTTOM)
        
        self.question_btn = []
        for i in range(len(self.questions)):
            self.question_btn.append(Button(self.button_frm,
                text=str(i+1),
                font="Arial, 25 bold",
                bg="darkorange",
                relief=RAISED,
                activebackground="yellow",
                command=lambda i=i: self.switch(i),
                width=3,
                borderwidth=5,
                highlightbackground="black",
                highlightthickness=3
            ))
            self.question_btn[i].pack(
                side=LEFT,
                padx=20,
                pady=(0, 50)
            )

    def _build_question_labels(self):
        self.question_lbl = Label(self, textvariable=self.current_str, font="Helvetica, 30 bold", anchor="center")
        self.question_lbl.pack(side=TOP, pady=(150, 0))
        
        self.result_lbl = Label(self, text="", font="Helvetica, 24 italic",anchor="center") #TODO: is the empty textreally useful here ?
        self.result_lbl.pack()

    def _build_answer_widget(self):
        self.valid_img = PhotoImage(file="valid.png")
        
        self.answer_frm = Frame(self)
        self.answer_frm.pack(side=TOP)

        self.answer_ent = Entry(self.answer_frm, font="Arial, 22", justify=CENTER, fg="white", bg="black", highlightthickness=0, borderwidth=5, insertbackground="grey")
        self.answer_ent.pack( side=LEFT, padx=(40, 0))

        self.validate_btn = Button(self.answer_frm,
            image=self.valid_img,
            font="Arial, 26",
            relief="ridge",
            borderwidth=7,
            bg="darkred",
            activebackground="red",
            command=self.validate,
            state="normal"
        )
        self.validate_btn.pack(side=RIGHT, pady=20, padx=(10, 20))

        self.validate_lbl = Label(self, textvariable=self.validate_str, font="Arial, 22 italic")
        self.validate_lbl.pack( side=TOP, pady=30)

    #Callback function to randomize the background color of all the elements
    def randomize_bg(self):
        #the hell is this built-in function <- it returns a hexadecimal string of the number you passed
        ran_color = hex(random.randint(0, 4194303)) #The magic number is 0xFFFFFF in decimal, as random.randint can only use decimal
        bg_color = "#" + ran_color[2:].zfill(6)    #The bg attribute of tkinter requires colors in the form of #000A1E
        
        self.configure(bg=bg_color)
        self.button_frm.config(bg=bg_color)
        self.question_lbl.config(bg=bg_color)
        self.result_lbl.config(bg=bg_color)
        self.answer_frm.config(bg=bg_color)
        self.validate_btn.config(highlightbackground=bg_color)
        self.validate_lbl.config(bg=bg_color)

    #Callback function to change the current question to the selected one
    def switch(self, num):
        self.current_str.set(self.questions[num]["question_str"])
        
        self.question_btn[current_num].config(state="normal")
        self.question_btn[current_num].config(relief=RAISED)
        
        self.current_num = num
        
        self.question_btn[current_num].config(state="disabled")
        self.question_btn[current_num].config(relief=SUNKEN)
        
        self.validate_str.set("")
        
        self.answer_ent.delete(0, END)
        
        self.randomize_bg()
        
        if questions[current_num]["completed"]:
            self.validate_btn.config(state="disabled")
            self.result_lbl.config(text=questions[current_num]["result"])
        else:
            self.validate_btn.config(state="active")
            self.result_lbl.config(text="")

    #Validate the answer to the question
    def validate():
        if self.answer_ent.get().casefold() == questions[current_num]["answer"].casefold():
            self.questions[current_num]["completed"]=True
            self.result_lbl.config(text=questions[current_num].result)
            self.validate_str.set("Correct")
            self.validate_lbl.config(fg="darkgreen")
            self.validate_btn.config(state="disabled")
            self.question_btn[current_num].config(bg="#00ff00")
        else:
            self.validate_str.set("Faux")
            self.validate_lbl.config(fg="red")

app = App()
app.mainloop()

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

progress.mainloop()
'''
