import csv
import json
import logging
import os
import re

from tqdm import tqdm

from constants import DATA_DIR, LOG_DIR, RESULTS_DIR

CSV_FILE_PATH = '{path}/{name}.csv'
JSON_FILE_PATH = '{path}/{name}.json'
LOG_FILE_PATH = '{path}/{name}.log'

CONVERT_STARTED = 'Началось преобразование файла: {name}.сsv'
CONVERT_SUCCESSFUL = 'Успешно преобразовался файла: {name}.csv'
CHECKING_JSON_START = 'Началась проверка файла json: {name}.json'
CHECKING_JSON_END = 'Закончилась проверка файла json: {name}.json'

ERROR_IN_LINE = 'Ошибка в строке {index}: {error}'


def csv_to_json(name_file):
    logging.info(CONVERT_STARTED.format(name=name_file))
    RESULTS_DIR.mkdir(exist_ok=True)
    with open(
        file=CSV_FILE_PATH.format(path=DATA_DIR, name=name_file),
        mode='r',
        encoding='utf-8'
    ) as csv_file:
        csv_reqder = csv.DictReader(csv_file)
        json_data = list(csv_reqder)

    with open(
        file=JSON_FILE_PATH.format(path=RESULTS_DIR, name=name_file),
        mode='w',
        encoding='utf-8'
    ) as json_file:
        json.dump(
            json_data,
            json_file,
            skipkeys=True,
            ensure_ascii=False,
            allow_nan=False,
            indent=4
        )
    logging.info(CONVERT_SUCCESSFUL.format(name=name_file))


def getting_files(folder_path, search_template,):
    return [
        os.path.splitext(file)[0]
        for file in os.listdir(folder_path)
        if re.compile(rf'{search_template}').search(file)
    ]


def checking_json_data(name_file):
    logging.info(CHECKING_JSON_START.format(name=name_file))
    logger = logging.getLogger(name_file)
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(
        LOG_FILE_PATH.format(path=LOG_DIR, name=name_file),
        mode='w',
        encoding='utf8'
    )
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.propagate = False
    logger.addHandler(handler)

    with open(
        file=JSON_FILE_PATH.format(path=RESULTS_DIR, name=name_file),
        mode='r',
        encoding='utf-8'
    ) as json_file:
        for index, data in tqdm(enumerate(json_file, start=1)):
            try:
                json_data = json.loads(data)
                isinstance(json_data, str)
            except (json.JSONDecodeError, ValueError) as error:
                logger.warning(
                    ERROR_IN_LINE.format(index=index, error=error)
                )
    logging.info(CHECKING_JSON_END.format(name=name_file))
