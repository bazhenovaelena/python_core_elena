from functools import wraps

def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Тест {func.__name__} завершён")
        print(f"Результат: {result}")
        return result
    return wrapper

@log_test
def correct_status(status):
    valid_statuses = ["PASS", "FAIL", "SKIP"]
    if status not in valid_statuses:
        print("Неизвестный статус")
    else:
        print("Корректный статус")
    return status

correct_status("PASS")

