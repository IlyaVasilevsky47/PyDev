import argparse
import logging

from dotenv import load_dotenv

from constants import DT_FORMAT, LOG_DIR, LOG_FILE, LOG_FORMAT

load_dotenv()


def configure_logging():
    LOG_DIR.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(LOG_FILE, mode='w')
    file_handler.setLevel(logging.INFO)
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(logging.StreamHandler(), file_handler)
    )


def configure_argument(available_modes):
    script = argparse.ArgumentParser(
        description='Скрипт выполняющий загрузку и преобразование данных',
        formatter_class=argparse.RawTextHelpFormatter
    )
    script.add_argument(
        'mode',
        choices=available_modes,
        help=(
            'Режимы работы: \n'
            '1. price-runner - Парсинг входного'
            'файла формата PriceRunner;\n'
            '2. inventory-runner - парсинг входного'
            'файла формата InventoryRunner.\n'
        )
    )
    return script
