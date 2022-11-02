from PyInquirer import prompt
from utils import append_list_as_row
import csv


def getUsers():
    users = []
    with open('users.csv', 'r') as f:
        reader = csv.reader(f)
        users = [line[0] for line in reader]
        # print(users)
    return users


def getExpenseQuestionsConfig():
    return [
        {
            "type": "input",
            "name": "label",
            "message": "New Expense - Label: ",
        },
        {
            "type": "list",
            "name": "spender",
            "message": "New Expense - Spender: ",
            "choices": getUsers(),
        },
    ]


def new_expense(*args):
    infos = prompt({
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    })
    try:
        float(infos["amount"])
    except ValueError:
        raise "Input Validation : Amount is not a number"

    infos = {
        **infos,
        **prompt(getExpenseQuestionsConfig())
    }

    # remove spender from users
    filteredUsers = [{"name": x} for x in getUsers() if x != infos["spender"]]
    infos = {
        **infos,
        **prompt({
            "type": "checkbox",
            "name": "other",
            "message": "Select Other Users Involved: ",
            "choices": filteredUsers,
        })
    }

    append_list_as_row("expense_report.csv", [
        infos["amount"],
        infos["label"],
        infos["spender"],
        *infos["other"]
    ])
    print("Expense Added !")
    return True
