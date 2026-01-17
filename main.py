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
        status_chosen = input("Пользователь:  ").strip().upper()
    print(f"Программа: Операции отфильтрованы по статусу {status_chosen}")


main()
