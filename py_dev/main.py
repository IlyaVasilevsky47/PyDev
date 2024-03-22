import logging

from configs import configure_argument, configure_logging
from constants import DATA_DIR
from utils import checking_json_data, csv_to_json, getting_files

SCRIPT_RUN = 'Скрипт запущен!'
COMMAND_LINE_ARGUMENT = 'Аргументы командной строки: {args}'
SCRIPT_END = 'Скрипт завершил работу.'


def inventory_convert(name_file='inventory'):
    for file in getting_files(DATA_DIR, name_file):
        csv_to_json(file)
        checking_json_data(file)


def price_convert(name_file='price'):
    for file in getting_files(DATA_DIR, name_file):
        csv_to_json(file)
        checking_json_data(file)


def hello():
    print('Я работа.')


MODE_TO_FUNCTION = {
    'inventory-convert': inventory_convert,
    'price-convert': price_convert,
    'db-import': hello,
    'db-export': hello,
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
