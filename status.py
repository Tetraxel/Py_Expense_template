from PyInquirer import prompt
from utils import append_list_as_row
import json
import csv

from utils import append_list_as_row


def show_status():
    debt = {}
    for user in list(csv.reader(open("users.csv"))):
        debt[user[0]] = {}

    # calculate report
    data = list(csv.reader(open("expense_report.csv")))
    for i, row in enumerate(data):
        spender = row[2]
        count = (len(row) - 2)
        amount = float(row[0]) / count
        for j, el in enumerate(row[3:]):
            otherSpender = el
            if spender not in debt[otherSpender].keys():
                debt[otherSpender][spender] = 0
            debt[otherSpender][spender] += amount

    # not working for now
    # # optimize
    # for key, row in debt.items():
    #     spender = row[2]

    #     for key3, val3 in row.items():
    #         # search spender occurences in other other
    #         for key2, row2 in debt.items():
    #             if key2 != key and key2 == key3:
    #                 if key in row2.keys():
    #                     print(val3, row2[key])
                    

    # print report
    for key, row in debt.items():
        print(f"{key} owes", end="")
        if len(row.keys()) == 0:
            print(" nothing", end="")
        else:
            for key, val in row.items():
                print(f" {val}€ to {key}", end="")
        print("")

    # print report
    report = []
    for key, row in debt.items():
        if len(row.keys()) != 0:
            for key2, val in row.items():
                report.append(f"{key} owes {val}€ to {key2}")

    filteredReport = [{"name": x} for x in report]
    infos = prompt({
        "type": "checkbox",
        "name": "other",
        "message": "Mark Debt payed",
        "choices": filteredReport,
    })
    return True
