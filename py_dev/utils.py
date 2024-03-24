import csv
import json
import logging
import os
import re

from tqdm import tqdm

from constants import DATA_DIR, LOG_DIR, RESULTS_DIR

CSV_FILE_PATH = '{path}\\{name}.csv'
JSON_FILE_PATH = '{path}\\{name}.json'
LOG_FILE_PATH = '{path}\\{name}.log'

CONVERT_STARTED = 'Началось преобразование файла: {name}.сsv'
CONVERT_SUCCESSFUL = 'Успешно преобразовался файла: {name}.csv'
INFORMATION_THE_FILE_JSON = 'Файл находиться: {path}'

ERROR_JSON = 'Error in line {index}: {error}, {values}'


def logger_warning(name_file):
    """Логирование и сбор WARNING"""
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
    return logger


def validation_check(name_file, format_fields, csv_reqder):
    """Проверка валидации полей"""
    logger = logger_warning(name_file)
    json_data = []
    for index, row in enumerate(csv_reqder, start=1):
        try:
            json_dict = {
                format[0]: format[1].action(data=value)
                for format, value in zip(format_fields.items(), row.values())
            }
            json_data.append(json_dict)
        except (json.JSONDecodeError, ValueError, TypeError) as error:
            logger.warning(ERROR_JSON.format(
                    index=index, error=error, values=row.values()
            ))
    return json_data


def csv_to_json(name_file, format_fields):
    """Переобразование формата .csv в .json"""
    logging.info(CONVERT_STARTED.format(name=name_file))
    RESULTS_DIR.mkdir(exist_ok=True)

    with tqdm(
        open(
            file=CSV_FILE_PATH.format(path=DATA_DIR, name=name_file),
            mode='r',
            encoding='utf-8',
        )
    ) as csv_file:
        json_data = validation_check(
            name_file, format_fields, csv.DictReader(csv_file)
        )

    with open(
        file=JSON_FILE_PATH.format(path=RESULTS_DIR, name=name_file),
        mode='w',
        encoding='utf-8',
    ) as json_file:
        json.dump(
            json_data, json_file, skipkeys=True, ensure_ascii=False, indent=4
        )
    logging.info(CONVERT_SUCCESSFUL.format(name=name_file))
    logging.info(
        INFORMATION_THE_FILE_JSON.format(
            path=JSON_FILE_PATH.format(path=RESULTS_DIR, name=name_file)
        )
    )


def getting_files(folder_path, search_template):
    """Поиск определеных файлов по имени"""
    return [
        os.path.splitext(file)[0]
        for file in os.listdir(folder_path)
        if re.compile(rf'{search_template}').search(file)
    ]
