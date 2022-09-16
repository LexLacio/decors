import datetime

def logger(some_function):
    def new_function(*args, **kwargs):
        result = some_function(*args, **kwargs)
        call_date = f'Дата и время вызова функции: {datetime.datetime.now()}'
        function_name = f'Имя функции: {some_function.__name__}'
        function_args = f'Аргументы функции: {args} и {kwargs}'
        function_result = f'Возвращаемое значение функции: {result}'
        data = f'{call_date}\n{function_name}\n{function_args}\n{function_result}\n'
        with open('logger1.txt','a', encoding='utf-8') as file:
            file.write(f'{data}\n')
        return result

    return new_function


@logger
def summator(a, b, c=100):
    return a + b + c


summator(3, 5)
