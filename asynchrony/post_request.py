# Подключаем библиотеки:
# 1. Используем встроенную асинхронную библиотеку
import asyncio
# 2. Для асинхронной работы HTTP запросов
#    устанавливаем новую библиотеку 'aiohttp'
import aiohttp

# 3. Для логирования буду использовать loguru для
#    лучшего логирования асинхронных функций
from loguru import logger

MESSAGE_RESPONSE = 'Url: {url}, Status: {status}, Data: {data}'


async def url_post(
    url: str, data: dict, session: aiohttp.ClientSession
):
    '''
    Функция выполняет отправку POST запроса по определенному адресу:
    - url - адрес;
    - data - данные для POST запроса;
    - session - интерфейс для отправки HTTP-запросов.
    '''
    # Создаем асинхронный контекстный менеджер для работы с ресурсами
    async with session.post(url, data=data) as response:
        # Получаем ответ от асинхронного метода
        # и получаем ответ от сервера в формате .json
        data = await response.json()
        logger.info(MESSAGE_RESPONSE.format(
            url=url, status=response.status, data=data
        ))


async def script():
    '''Основная асинхронная функция'''
    logger.info('Скрипт начал работу')

    # Список url
    urls = [
        "http://api.heado.ru/endpoint1",
        "http://api.heado.ru/endpoint2",
        "http://api.heado.ru/endpoint3",
        "http://api.heado.ru/endpoint4",
    ]

    # Данные в post запрос
    payload = {"key1": "value1", "key2": "value2"}

    # Список задач
    tasks = []

    # Следующий код создает новый экземпляр ClientSession
    # ClientSession представляет возможность отправки
    # асинхронных HTTP-запросов
    async with aiohttp.ClientSession() as session:
        # Цикл для добавления заданий
        for index in range(len(urls)):
            # Добавляем асинхронную задачу (coroutine)
            # которая отправляет POST запрос
            tasks.append(asyncio.create_task(
                url_post(urls[index], payload, session)
            ))
        # Данный асинхронный метод используется для ожидания
        # завершения нескольких асинхронных задач одновременно
        # и сбора их результатов
        await asyncio.gather(*tasks)
    logger.info('Скрипт завершил работу')


if __name__ == '__main__':
    # Запускам нашу асинхронную функцию script()
    asyncio.run(script())
