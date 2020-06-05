import datetime


# Task 1
def logger(func):
    start_time = datetime.datetime.utcnow()

    def wrapper(*args):
        result = func(*args)
        with open('my_logger_1.txt', 'w', encoding='utf8') as log_file:
            log_file.write(f'Время начала работы: {start_time} \n')
            log_file.write(f'Имя функции: {func.__name__} \n')
            log_file.write(f'Принимаемый аргумент: {args} \n')
            log_file.write(f'Возвращаемое значение: {result} \n')
            end_time = datetime.datetime.utcnow()
            work_time = end_time - start_time
            log_file.write(f'Время работы: {work_time}')
        return result

    return wrapper
