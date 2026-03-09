from pathlib import Path
import json

def main():
    current_dir = Path.cwd()
    question_file = current_dir / "questions.json"
    while True:
        try: 
            with open(question_file, "r", encoding="utf-8") as file:
                try:
                    json_object = json.load(file)
                except json.JSONDecodeError:
                   json_object = []
        except FileNotFoundError:
            file = open(question_file, "w", encoding="utf-8")
            file.close()
        while True:
            json_object = add_question(question_file, json_object)

def add_question(question_file, json_object):
    question_str = input('''Merci d'entrer le texte de votre question.
Respectez la casse et la ponctuation que vous voulez.
Pas besoin de mettre de guillemets, mettez juste votre texte exact.
Pas trop long!!! Une phrase au mieux.
>>>''')
    answer = input("Merci de faire la même chose avec votre réponse.\n>>>")

    new_question = {
        "question_str": question_str,
        "answer": answer,
        }
    json_object.append(new_question)
    with open(question_file, "w", encoding="utf-8") as fileWrite:
        json.dump(json_object, fileWrite, ensure_ascii=False, indent=4)

    print('''Merci, on a bien pris en compte votre question!
===============================================
''')
    return json_object

main()
