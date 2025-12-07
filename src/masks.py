def get_mask_card_number(card_number: str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    """
    if not card_number.isdigit() or len(card_number) != 16:
        return "Номер карты введен некорректно"
    else:
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """
    принимает на вход номер счета и возвращает его маску
    """
    if not account_number.isdigit() or account_number == "":
        return "Номер счета введен некорректно"
    else:
        return "**" + account_number[-4:]
