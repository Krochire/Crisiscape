#!/usr/bin/python

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
            add_question(json_object)
        elif choice == "2":
            edit_question(json_object)
        elif choice == "3":
            remove_question(json_object)
        else:
            print("Mauvaise entrée")
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(json_object, file, ensure_ascii=False, indent=4)

def get_choice():
    return input('''Choississez l'opération à effectuer:
    1. Ajouter une question
    2. Modifier une question
    3. Supprimer une question
Numéro de l'opération>>>''')

def add_question(json_object):
    question_str = input('''Merci d'entrer le texte de votre question.
Respectez la casse et la ponctuation que vous voulez.
Pas besoin de mettre de guillemets, mettez juste votre texte exact.
Pas trop long!!! Une phrase au mieux.
>>>''')
    answer = input("Merci de faire la même chose avec votre réponse.\n>>>")
    result = input("Merci de faire la même chose avec la phrase donnée après une bonne réponse.\n>>>")
    question_id = len(json_object)

    print('''Merci, on a bien pris en compte votre question!
===============================================''')
    new_question = {
        "question_str": question_str,
        "answer": answer,
        "id": question_id,
        "result": result
        }
    json_object.append(new_question)

def edit_question(json_object):
    list_questions(json_object)
    question_choice = None
    while True:
        try:
            question_choice = int(input("Entrez le numéro de la question à modifier.\n>>>"))
        except TypeError:
            print("Mauvaise entrée")
            continue
        break
    while True:
        edit_choice = input("Que voulez-vous modifier ? (Q/A/R)\n>>>")
        if edit_choice.casefold() == "q":
            json_object[question_choice]["question_str"] = input("Entrez votre nouvelle phrase.\n>>>")
        elif edit_choice.casefold() == "a":
            json_object[question_choice]["answer"] = input("Entrez votre nouvelle phrase.\n>>>")
        elif edit_choice.casefold() == "r":
            json_object[question_choice]["result"] = input("Entrez votre nouvelle phrase.\n>>>")
        else:
            print("Mauvaise entrée")
            continue
        break

def remove_question(json_object):
    list_questions(json_object)
    question_choice = None
    while True:
        try:
            question_choice = int(input("Entrez le numéro de la question à supprimer.\n>>>"))
        except TypeError:
            print("Mauvaise entrée")
            continue
        break
    confirmation = input("Cette action est irréversible, en êtes-vous sûr ? (Y/n)").casefold()
    if confirmation != "y":
        return
    json_object.pop(question_choice)
    for question_num in range(len(json_object)):
        json_object[question_num]["id"] = question_num

def list_questions(json_object):
    for question in json_object:
        print(f'''#{question["id"]}
    Q: {question["question_str"]}
    A: {question["answer"]}
    R: {question["result"]}
    ================================================''')

main()