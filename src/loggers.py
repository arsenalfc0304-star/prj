import logging

utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
utils_file_handler = logging.FileHandler("./logs/utils.log")
utils_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
utils_file_handler.setFormatter(utils_file_formatter)
utils_logger.addHandler(utils_file_handler)

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
masks_file_handler = logging.FileHandler("./logs/masks.log")
masks_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
masks_file_handler.setFormatter(masks_file_formatter)
masks_logger.addHandler(masks_file_handler)