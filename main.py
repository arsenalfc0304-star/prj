from src.utils import load_json
from src.csv_excel_readers import read_data_from_csv, read_data_from_excel
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.widget import mask_account_card
from datetime import datetime


def main():
    print("Программа: Привет! Добро пожаловать в программу работы\n" "с банковскими транзакциями.")
    # 1 выбор источника данных
    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    sources_allowed = {"1": "JSON", "2": "CSV", "3": "XLSX"}
    source_chosen = input("Пользователь:  ").strip()

    while source_chosen not in sources_allowed.keys():
        print("Программа: Пункт меню выбран не корректно. Введите 1 или 2 или 3.\n")
        source_chosen = input("Пользователь:  ").strip()
    print(f"Программа: Для обработки выбран {sources_allowed[source_chosen]}-файл.")

    # 2 выбор статуса транзакций
    print(
        "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    statuses_allowed = ("EXECUTED", "CANCELED", "PENDING")
    status_chosen = input("Пользователь:  ").strip()

    while status_chosen.upper() not in statuses_allowed:
        print(
            f"Программа: Статус операции \"{status_chosen}\" недоступен.\n"
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        status_chosen = input("Пользователь:  ").strip()
    print(f"Программа: Операции отфильтрованы по статусу \"{status_chosen.upper()}\"")

    # 3 запрос сортировки по дате
    print("Программа: Отсортировать операции по дате? Да/Нет")
    is_sorted_by_date = input("Пользователь:  ").strip()
    while is_sorted_by_date.lower() not in ("да", "нет"):
        print("Программа: Ответ некорректный. Отсортировать операции по дате? Да/Нет")
        is_sorted_by_date = input("Пользователь:  ").strip()

    if is_sorted_by_date.lower() == "да":
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        is_sorted_descending = input("Пользователь:  ")
        while is_sorted_descending.lower() not in ("по возрастанию", "по убыванию"):
            print("Программа: Ответ некорректный. Отсортировать по возрастанию или по убыванию?")
            is_sorted_descending = input("Пользователь:  ")

    # 4 запрос валюты
    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    only_rub_transactions = input("Пользователь:  ").strip()
    while only_rub_transactions.lower() not in ("да", "нет"):
        print("Программа: Ответ некорректный. Выводить только рублевые транзакции? Да/Нет")
        only_rub_transactions = input("Пользователь:  ").strip()

    # запрос фильтрации по слову
    print(
        "Программа: Отфильтровать список транзакций по определенному слову\n"
        "в описании? Да/Нет"
    )
    with_filter = input("Пользователь:  ").strip()
    while with_filter.lower() not in ("да", "нет"):
        print("Программа: Ответ некорректный. Отфильтровать список транзакций\n"
              "по определенному слову в описании? Да/Нет")
        with_filter = input("Пользователь:  ").strip()

    if with_filter.lower() == "да":
        print("Программа: Введите слово")
        key_word = input("Пользователь:  ").strip()

    # вывод результата
    if source_chosen == "1":
        result_1 = load_json("data/operations.json")
    elif source_chosen == "2":
        result_1 = read_data_from_csv("data/transactions.csv")
    elif source_chosen == "3":
        result_1 = read_data_from_excel("data/transactions_excel.xlsx")

    result_2 = filter_by_state(result_1, status_chosen.upper())

    if is_sorted_by_date == "да":
        result_3 = sort_by_date(result_2, descending=(is_sorted_descending == "по убыванию"))
    else:
        result_3 = result_2

    if only_rub_transactions.lower() == "да":
        result_4 = process_bank_search(result_3, "RUB")
    else:
        result_4 = result_3

    if with_filter.lower() == "да":
        result_5 = process_bank_search(result_4, key_word)
    else:
        result_5 = result_4

    print("Программа: Распечатываю итоговый список транзакций...")

    if len(result_5) > 0:
        print("Программа:\n"
              f"Всего банковских операций в выборке: {len(result_5)}\n"
        )
        for transaction in result_5:
            print(
                f"{transaction['date'][8:10]}.{transaction['date'][5:7]}.{transaction['date'][0:4]} {transaction['description']}\n"
                f"{mask_account_card(transaction['to'])}\n"
                f"Сумма: {transaction['amount']} {transaction['currency']['name']}"
            )
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

main()
