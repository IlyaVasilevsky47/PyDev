# PyDev
Py-Dev - это удобный инструмент, написанный на Python, предназначенный для загрузки и преобразования данных. Этот скрипт обладает рядом функциональных возможностей, которые облегчают работу с данными.

## Основные возможности:
### price-runner:
- В этом режиме скрипт выполняет парсинг входного файла в формате [PriceRunner](https://support.heado.ru/api/management/#method_priceupdatebatch) для файлов с именем `price` и форматом CSV, а затем преобразует его в JSON.

### inventory-runner:
- В этом режиме скрипт выполняет парсинг входного файла в формате [InventoryRunner](https://support.heado.ru/api/management/#method_inventoryUpdateBatch) для файлов с именем `inventor` и форматом CSV, а затем преобразует его в JSON.

### В проекте используются три файла CSV и их соответствующие представления в формате JSON для обработки данных:
- `price.csv`
- `inventory1.csv`
- `inventory2.csv`

### После преобразования данные сохраняются в формате JSON:
- `price.json`
- `inventory1.json`
- `inventory2.json`

### В проекте реализована функция логирования для каждого JSON-файла с целью проверки типов данных и синтаксических ошибок:
- `price.log`
- `inventory1.log`
- `inventory2.log`

### Основные логи процесса собираются в:
- `main.log`

## Запуск проекта:
1. Клонируем проект.
```bash
    git git@github.com:IlyaVasilevsky47/PyDev.git
```
2. Создаем и запускаем виртуальное окружение.
```bash
    python -m venv venv
    source venv/scripts/activate
```
3. Обновляем менеджер пакетов pip и устанавливаем зависимости из файла requirements.txt.
```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```
4. Переходи в папку и запускаем проект.
```bash
    cd py_dev
    python main.py -h
```

## Возможности программы:
```bash
    usage: main.py [-h] {price-runner,inventory-runner}

    Скрипт выполняющий загрузку и преобразование данных

    positional arguments:
    {price-runner,inventory-runner}
                            Режимы работы:
                            1. price-runner - парсинг входногофайла формата PriceRunner;
                            2. inventory-runner - парсинг входногофайла формата InventoryRunner.

    options:
    -h, --help            show this help message and exit
```

## Автор:
- Василевский И.А.
- [Почта](vasilevskijila047@gmail.com)
- [Вконтакте](https://vk.com/ilya.vasilevskiy47)

## Технический стек
- Python 3.11.0
- Tqdm 4.66.2
