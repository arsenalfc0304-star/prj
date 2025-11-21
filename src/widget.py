from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """
    принимает на вход номер карты или счета и возвращает его маску
    """
    if "Visa Platinum" in number:
        return "Visa Platinum " + get_mask_card_number(number.replace("Visa Platinum ", ""))
    elif "Maestro" in number:
        return "Maestro " + get_mask_card_number(number.replace("Maestro ", ""))
    elif "Счет" in number:
        return "Счет " + get_mask_account(number.replace("Счет ", ""))
    else:
        return "Номер введен некорректно"


def get_date(date: str) -> str:
    """
    принимает на вход строку с датой в формате "ГГГГ-ММ-ДДT02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    return date[8:10] + "." + date[5:7] + "." + date[0:4]
