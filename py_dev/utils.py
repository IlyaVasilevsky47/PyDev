import csv
import json
import logging
import os
import re
from datetime import datetime
from tqdm import tqdm

from constants import DATA_DIR, LOG_DIR, RESULTS_DIR, DATE_FORMATS

CSV_FILE_PATH = '{path}\\{name}.csv'
JSON_FILE_PATH = '{path}\\{name}.json'
LOG_FILE_PATH = '{path}\\{name}.log'

CONVERT_STARTED = 'Началось преобразование файла: {name}.сsv'
CONVERT_SUCCESSFUL = 'Успешно преобразовался файла: {name}.csv'
INFORMATION_THE_FILE_JSON = 'Файл находиться: {path}'

ERROR_JSON = 'Error in line {index}: {error}, {values}'


def logger_json_data(name_file):
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


def csv_to_json(name_file, format_fields):
    logging.info(CONVERT_STARTED.format(name=name_file))
    RESULTS_DIR.mkdir(exist_ok=True)
    logger = logger_json_data(name_file)

    json_data = []
    with tqdm(open(
        file=CSV_FILE_PATH.format(path=DATA_DIR, name=name_file),
        mode='r',
        encoding='utf-8'
    )) as csv_file:
        csv_reqder = csv.DictReader(csv_file)
        for index, row in enumerate(csv_reqder, start=1):
            try:
                json_dict = {
                    format[0]: format[1](value)
                    for format, value
                    in zip(format_fields, row.values())
                }
                json_data.append(json_dict)
            except (json.JSONDecodeError, ValueError, TypeError) as error:
                logger.warning(ERROR_JSON.format(
                        index=index,
                        error=error,
                        values=row.values()
                ))

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
            indent=4
        )
    logging.info(CONVERT_SUCCESSFUL.format(name=name_file))
    logging.info(
        INFORMATION_THE_FILE_JSON.format(
            path=JSON_FILE_PATH.format(path=RESULTS_DIR, name=name_file))
        )


def getting_files(folder_path, search_template,):
    return [
        os.path.splitext(file)[0]
        for file in os.listdir(folder_path)
        if re.compile(rf'{search_template}').search(file)
    ]


def convert_date(datetime_str):
    for date_formate in DATE_FORMATS:
        try:
            datetime.strptime(datetime_str, date_formate)
            return datetime_str
        except ValueError:
            pass
    raise ValueError('no valid date format found')


def checking_empty_field(variable):
    if variable in '':
        return 'null'
    return variable
