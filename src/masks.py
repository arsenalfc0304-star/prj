from loggers import masks_logger

def get_mask_card_number(card_number: str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    """
    if not card_number.isdigit() or len(card_number) != 16 or card_number[0] == 0:
        masks_logger.error(f'номер карты введен некорректно')
        return "Номер карты введен некорректно"
    else:
        masks_logger.info(f'номер карты маскирован')
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """
    принимает на вход номер счета и возвращает его маску
    """
    if not account_number.isdigit() or account_number == "":
        masks_logger.error(f'номер счета введен некорректно')
        return "Номер счета введен некорректно"
    else:
        masks_logger.info(f'номер счета маскирован')
        return "**" + account_number[-4:]
