from src.masks import get_mask_account, get_mask_card_number

pay_cards = (
    "Visa Classic",
    "Visa Gold",
    "Visa Platinum",
    "Visa",
    "MasterCard",
    "Maestro",
    "American Express",
    "Discover",
    "МИР",
)


def mask_account_card(number: str) -> str:
    """
    принимает на вход номер карты или счета и возвращает его маску
    """
    for card in pay_cards:
        if card.lower() in number.lower():
            return f"{number[0:len(card)]} {get_mask_card_number(number[len(card):].strip())}"
    if "Счет".lower() in number.lower():
        return f"{number[0:len("Счет")]} {get_mask_account(number[len("Счет"):].strip())}"
    else:
        return ""  # "Номер введен некорректно"


def get_date(date: str) -> str:
    """
    принимает на вход строку с датой в формате "ГГГГ-ММ-ДДT02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    if (
        len(date) >= 10
        and date[4] == "-"
        and date[7] == "-"
        and date[0:4].isdigit()
        and date[5:7].isdigit()
        and int(date[5:7]) <= 12
        and date[8:10].isdigit()
    ) and int(date[8:10]) <= 31:
        return date[8:10] + "." + date[5:7] + "." + date[0:4]
    else:
        return "Дата введена некорректно"
