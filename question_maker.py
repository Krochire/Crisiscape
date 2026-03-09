import json

def main():
    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            json_object = json.load(file)
    except FileNotFoundError:
        file = open("questions.json", "w", encoding="utf-8")
        json_object = []
        json.dump(json_object, file, ensure_ascii=False, indent=4)
        file.close()
    while True:
        choice = get_choice()
        print("=========================")
        if choice == "save":
            break
        elif choice == "1":
            json_object.append(add_question(len(json_object)))
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(json_object, file, ensure_ascii=False, indent=4)

def get_choice():
    return input('''Choississez l'opération à effectuer:
    1. Ajouter une question
    2. Modifier une question
    3. Supprimer une question
Numéro de l'opération>>>''')

def add_question(question_number):
    question_str = input('''Merci d'entrer le texte de votre question.
Respectez la casse et la ponctuation que vous voulez.
Pas besoin de mettre de guillemets, mettez juste votre texte exact.
Pas trop long!!! Une phrase au mieux.
>>>''')
    answer = input("Merci de faire la même chose avec votre réponse.\n>>>")
    question_id = question_number + 1

    print('''Merci, on a bien pris en compte votre question!
===============================================''')
    return {
        "question_str": question_str,
        "answer": answer,
        "id": question_id,
        }

main()
