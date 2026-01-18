from src.utils import load_json
from src.csv_excel_readers import read_data_from_csv, read_data_from_excel

def main():
    print("Программа: Привет! Добро пожаловать в программу работы\n" "с банковскими транзакциями.")
    # выбор источника данных
    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    sources_allowed = {1: "JSON", 2: "CSV", 3: "XLSX"}
    source_chosen = input("Пользователь:  ").strip()

    while int(source_chosen) not in sources_allowed.keys():
        print("Программа: Пункт меню выбран не корректно. Введите 1 или 2 или 3.\n")
        source_chosen = input("Пользователь:  ").strip()
    print(f"Программа: Для обработки выбран {sources_allowed[int(source_chosen)]}-файл.")

    # выбор статуса транзакций
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

    # запрос сортировки по дате
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

    # запрос валюты
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

    # вывод результата
    print("Программа: Распечатываю итоговый список транзакций...")
    print("Программа:\n"
          "Всего банковских операций в выборке: 4"
          )



main()
