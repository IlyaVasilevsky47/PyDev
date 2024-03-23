import logging

from configs import configure_argument, configure_logging
from constants import DATA_DIR
from tables import INVENTORY_FORMAT, PRICE_FORMAT
from utils import csv_to_json, getting_files

SCRIPT_RUN = 'Скрипт запущен!'
COMMAND_LINE_ARGUMENT = 'Аргументы командной строки: {args}'
SCRIPT_END = 'Скрипт завершил работу.'


def price_runner(name_file='price', format_fields=PRICE_FORMAT):
    """Переобразвания файлов с именем price .csv из .json"""
    for file in getting_files(DATA_DIR, name_file):
        csv_to_json(file, format_fields)


def inventory_runner(name_file='inventory', format_fields=INVENTORY_FORMAT):
    format
    """Переобразвания файлов с именем inventory .csv из .json"""
    for file in getting_files(DATA_DIR, name_file):
        csv_to_json(file, format_fields)


MODE_TO_FUNCTION = {
    'price-runner': price_runner,
    'inventory-runner': inventory_runner,
}


def main():
    configure_logging()
    args = configure_argument(MODE_TO_FUNCTION.keys()).parse_args()
    logging.info(SCRIPT_RUN)
    logging.info(COMMAND_LINE_ARGUMENT.format(args=args))
    try:
        MODE_TO_FUNCTION[args.mode]()
    except Exception as error:
        logging.error(error, exc_info=True)
    logging.info(SCRIPT_END)


if __name__ == '__main__':
    main()
