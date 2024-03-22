import logging

from configs import configure_argument, configure_logging
from constants import DATA_DIR
from utils import csv_to_json, getting_files
from tables import PRICE_FORMAT, INVENTORY_FORMAT

SCRIPT_RUN = 'Скрипт запущен!'
COMMAND_LINE_ARGUMENT = 'Аргументы командной строки: {args}'
SCRIPT_END = 'Скрипт завершил работу.'


def price_runner(name_file='price'):
    for file in getting_files(DATA_DIR, name_file):
        csv_to_json(file, PRICE_FORMAT)


def inventory_runner(name_file='inventory'):
    for file in getting_files(DATA_DIR, name_file):
        csv_to_json(file, INVENTORY_FORMAT)


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
