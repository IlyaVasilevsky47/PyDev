import argparse
import logging
import os

from dotenv import load_dotenv

from constants import DT_FORMAT, LOG_DIR, LOG_FILE, LOG_FORMAT

load_dotenv()


class Settings:
    POSTGRES_NAME = 'postgres'
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = int(os.getenv('DB_PORT'))


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
            '1. inventory-convert - перебразовует из csv в json '
            'для таблицы inventory; \n'
            '2. price-convert - перебразовует из csv в json'
            'для таблицы price.\n'
            '\nДополнительные режимы (трубеться запуск docker-compose):\n'
            '1. db-import - импортируем данные csv в базу данных;\n'
            '2. db-export - экспортируем данные из базы данных в json.'
        )
    )
    return script
