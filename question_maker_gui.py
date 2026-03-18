import tkinter as tk
import json

root = tk.Tk()
root.geometry("1280x720")
root.maxsize(1280, 720)
root.title("Créateur de question 1.0")
root.config(bg="steelblue")

try:
    with open("questions.json", "r", encoding="utf-8") as file:
        json_object = json.load(file)
except FileNotFoundError:
    file = open("questions.json", "w", encoding="utf-8")
    json_object = []
    json.dump(json_object, file, ensure_ascii=False, indent=4)
    file.close()

# These functions are used by various buttons to bring up the corresponding form
def add_question():
    pass

def save():
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(json_object, file, ensure_ascii=False, indent=4)
    root.destroy()

# This frame is the main menu
choice_frm = tk.Frame(
    root,
    bg="skyblue",
)

title_lbl= tk.Label(
    choice_frm,
    bg="skyblue",
    text="GUI pour la création de question",
    font=("Arial", 24)
)

add_btn = tk.Button(
    choice_frm,
    bg="lightgray",
    font="Arial",
    text="Ajouter une question",
    command=add_question,
    width=26,
    height=1
)

edit_btn = tk.Button(
    choice_frm,
    bg="lightgray",
    font="Arial",
    text="Mettre à jour une question",
    command=lambda: print("Pressed"),
    width=26,
    height=1
)

remove_btn = tk.Button(
    choice_frm,
    bg="lightgray",
    font="Arial",
    text="Retirer une question",
    command=lambda: print("Pressed"),
    width=26,
    height=1
)

save_btn = tk.Button(
    choice_frm,
    bg="lightgray",
    font="Arial",
    text="Sauvegarder et quitter",
    command=save,
    width=20,
    height=1
)

choice_frm.pack(side="left", anchor="center", padx=10, pady=10, fill="both", expand=True)

title_lbl.pack(pady=20)
add_btn.pack(pady=10)
edit_btn.pack(pady=50)
remove_btn.pack(pady=10)
save_btn.pack(side="bottom", pady=10)

# This frame is the question adding form

root.mainloop()
