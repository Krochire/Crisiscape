import tkinter as tk
import json

root = tk.Tk()
root.geometry("1280x720")
root.maxsize(1280, 720)
root.title("Créateur de question 1.0")
#root.config(bg="steelblue")

try:
    with open("questions.json", "r", encoding="utf-8") as file:
        json_object = json.load(file)
except FileNotFoundError:
    file = open("questions.json", "w", encoding="utf-8")
    json_object = []
    json.dump(json_object, file, ensure_ascii=False, indent=4)
    file.close()

# Helper functions
# ================
# This function is used by various buttons to bring up the corresponding form
def change_frame(show, hide=None):
    if hide:
        hide.pack_forget()
    show.pack(
        side="left",
        anchor="center",
        fill="both",
        expand=True
    )

def make_question():
    question_str = question_ent.get()
    answer = answer_ent.get()
    result = result_ent.get()
    question_id = len(json_object)

    if question_str == "" or answer == "" or result == "":
        info_lbl.config(text="Tous les champs doivent être remplis!", fg="red")
        return False

    new_question = {
        "question_str": question_str,
        "answer": answer,
        "id": question_id,
        "result": result
    }
    print(new_question)
    return new_question

# Callback functions
# ==================
# Callback function to handle listbox selection
def handle_listbox_select(event):
    global selected_question
    selected_question, = question_lst.curselection()
    delete_btn.config(state="active")
    edit_btn.config(state="active")

# Callback function to reset the question form
def reset_question_form(event):
    info_lbl.config(text="")
    question_ent.delete(0, tk.END)
    answer_ent.delete(0, tk.END)
    result_ent.delete(0, tk.END)

# Question form functions
# =======================
# Sets up the question form in add mode
def add_mode():
    submit_btn.config(command=add_question)
    return_btn.config(command=lambda: change_frame(menu_frm, question_form_frm))
    change_frame(question_form_frm, menu_frm)

# Adds a new question to the JSON data by taking data entered in the entries
def add_question():
    new_question = make_question()
    if not new_question:
        return

    json_object.append(new_question)

    question_ent.delete(0, tk.END)
    answer_ent.delete(0, tk.END)
    result_ent.delete(0, tk.END)
    info_lbl.config(text="Soumis!", fg="green")

# Sets up the question form in edit mode
def edit_mode(index):
    question_ent.insert(0, json_object[index]["question_str"])
    answer_ent.insert(0, json_object[index]["answer"])
    result_ent.insert(0, json_object[index]["result"])
    submit_btn.config(command=lambda: edit_question(selected_question))
    return_btn.config(command=lambda: review_question(question_form_frm))
    change_frame(question_form_frm, review_frm)

# Edits an existing question in the question data
def edit_question(index):
    new_question = make_question()
    if not new_question:
        return

    json_object[index] = {
            "question_str": question_str,
            "answer": answer,
            "id": index,
            "result": result
        }

    question_ent.delete(0, tk.END)
    answer_ent.delete(0, tk.END)
    result_ent.delete(0, tk.END)
    review_question(question_form_frm)

# Misc functions
# ==============
# Populates list_variable and shows the question review form, called by a button in menu_frm
def review_question(hide):
    questions = [
        f"Question {q["id"]}: {q["question_str"]}"
        for q in json_object
    ]
    list_variable.set(tuple(questions))

    change_frame(review_frm, hide)

# Called by a button in delete_frm
def delete_question(index):
    json_object.pop(index)
    review_question(delete_frm)
    delete_btn.config(state="disabled")
    edit_btn.config(state="disabled")

# Called by the quit button to save changes and exit the program
def save():
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(json_object, file, ensure_ascii=False, indent=4)
    root.destroy()

# ================================================================

# This frame is the main menu
menu_frm = tk.Frame(
    root
)

tk.Label(
    menu_frm,
    text="GUI pour la création de question",
    font=("Arial", 24)
).pack(pady=20)

tk.Button(
    menu_frm,
    font="Arial",
    text="Ajouter une question",
    command=add_mode,
    width=26,
    height=1
).pack(pady=10)

tk.Button(
    menu_frm,
    font="Arial",
    text="Mettre à jour une question",
    command=lambda: review_question(menu_frm),
    width=26,
    height=1
).pack(pady=50)

tk.Button(
    menu_frm,
    font="Arial",
    text="Sauvegarder et quitter",
    command=save,
    width=20,
    height=1
).pack(side="bottom", pady=10)

# This frame is the question adding/editing form
question_form_frm = tk.Frame(
    root
)

tk.Label(
    question_form_frm,
    text="Texte de la question :",
    font="Arial"
).pack()

question_ent = tk.Entry(
    question_form_frm,
    font="Arial"
)
question_ent.pack()

tk.Label(
    question_form_frm,
    text="Texte de la réponse :",
    font="Arial"
).pack()

answer_ent = tk.Entry(
    question_form_frm,
    font="Arial"
)
answer_ent.pack()

tk.Label(
    question_form_frm,
    text="Texte du résultat :",
    font="Arial"
).pack()

result_ent = tk.Entry(
    question_form_frm,
    font="Arial"
)
result_ent.pack()

info_lbl = tk.Label(
    question_form_frm,
    text="",
    font="Arial"
)
info_lbl.pack()

submit_btn = tk.Button(
    question_form_frm,
    font="Arial",
    text="Soumettre",
)
submit_btn.pack()

return_btn = tk.Button(
    question_form_frm,
    font="Arial",
    text="Retour",
)
return_btn.pack()
return_btn.bind("<Button>", reset_question_form)

# This frame is used to review questions
review_frm = tk.Frame(
    root
)

#Check review_questions for how this is handled
list_variable = tk.Variable()
selected_question = None
question_lst = tk.Listbox(
    review_frm,
    selectmode=tk.BROWSE,
    listvariable=list_variable
)
question_lst.pack()
question_lst.bind('<<ListboxSelect>>', handle_listbox_select)

edit_btn = tk.Button(
    review_frm,
    text="Modifier",
    font="Arial",
    command=lambda: edit_mode(selected_question),
    state="disabled"
)
edit_btn.pack()

delete_btn = tk.Button(
    review_frm,
    text="Supprimer",
    font="Arial",
    command=lambda: change_frame(delete_frm, review_frm),
    state="disabled"
)
delete_btn.pack()

tk.Button(
    review_frm,
    font="Arial",
    text="Retour",
    command=lambda: change_frame(menu_frm, review_frm)
).pack()

# This frame is the question deleting confirmation
delete_frm = tk.Frame(
    root
)

tk.Label(
    delete_frm,
    text="Êtes-vous sûr de vouloir supprimer cette question ?\nCette action est irréversible.",
    font="Arial"
).pack()

tk.Button(
    delete_frm,
    text="Non",
    font="Arial",
    command=lambda: change_frame(review_frm, delete_frm)
).pack()

tk.Button(
    delete_frm,
    text="Oui",
    font="Arial",
    command=lambda: delete_question(selected_question)
).pack()

change_frame(menu_frm)
root.mainloop()
