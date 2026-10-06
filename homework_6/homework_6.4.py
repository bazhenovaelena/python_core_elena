import random

def repeat(n):
    def decorator(func):
        def wrapper(number):
            for i in range(1, n+1):
                print(f"Попытка: {i}")
                result = func(number)
                if result:  # если успех — выходим из цикла
                    break
        return wrapper
    return decorator


@repeat(9)
def correct_number(number):
    x = random.randint(1,5)
    if x == number:
        print(f"{number} True")
        return True
    else:
        print(f"{number} False")
        return False

correct_number(4)
