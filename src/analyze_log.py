import csv
from collections import Counter
import os


def reader_file(data):
    with open(data, mode='r') as file:
        log_list = list(csv.reader(file))
        return log_list


def most_requested_by_client(client, data):
    log_list = reader_file(data)
    client_list = list()
    for log in log_list:
        if log[0] == client:
            client_list.append(log[1])
    return Counter(client_list).most_common(1)[0][0]


def most_requested_by_client_and_food(client, food, data):
    log_list = reader_file(data)
    food_counter = 0
    for log in log_list:
        if log[0] == client and log[1] == food:
            food_counter += 1
    return food_counter


def never_requested_by_client(client, data):
    log_list = reader_file(data)
    food_list = set()
    food_client = set()
    for food in log_list:
        food_list.add(food[1])
        if food[0] == client:
            food_client.add(food[1])
    return food_list - food_client


def never_go_by_client(client, data):
    log_list = reader_file(data)
    days_list = set()
    days_client = set()
    for day in log_list:
        days_list.add(day[2])
        if day[0] == client:
            days_client.add(day[2])
    return days_list - days_client


def writer_txt(file_client):
    with open("data/mkt_campaign.txt", mode="w") as file:
        for client in file_client:
            print(client, file=file)


def analyze_log(path_to_file):
    if not os.path.exists(path_to_file) or not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    maria = most_requested_by_client("maria", path_to_file)
    arnaldo = most_requested_by_client_and_food(
        "arnaldo", "hamburguer", path_to_file)
    joao = never_requested_by_client("joao", path_to_file)
    joao_1 = never_go_by_client("joao", path_to_file)

    writer_txt([maria, arnaldo, joao, joao_1])
