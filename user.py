from PyInquirer import prompt
from utils import append_list_as_row

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New Name - Name: ",
    },
]


def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    append_list_as_row("users.csv", [
        infos["name"],
    ])
    print("User Added !")
    return True
