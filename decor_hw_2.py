import os
import datetime


def logger(logs_folder: object) -> object:
    """
    Декоратор Логгер.
    Логи по вызываемой функции запишутся в файл logger.txt.
    Нужно указать существующую папку куда запишется файл logger.txt.
    Относительный путь к файлу построится автоматически.

    """

    def logger_body(some_function):
        def new_function(*args, **kwargs):
            result = some_function(*args, **kwargs)

            call_date = f'Дата и время вызова функции: {datetime.datetime.now()}'
            function_name = f'Имя функции: {some_function.__name__}'
            function_args = f'Аргументы функции: {args} и {kwargs}'
            function_result = f'Возвращаемое значение функции: {result}'
            data = f'{call_date}\n{function_name}\n{function_args}\n{function_result}\n'

            base_path = os.getcwd()
            file_name = 'logger2.txt'
            full_path = os.path.join(base_path, logs_folder, file_name)

            with open(full_path, 'a', encoding='utf-8') as file:
                file.write(f'{data}\n')

            return result

        return new_function

    return logger_body


@logger('logs2')
def summator(a, b):
    return a + b


summator(3, b=5)
