def run_test(retries, timeout):

    if retries < 0 or retries > 5:
        raise ValueError ("Недопустимое количество запусков")

    if timeout <= 0:
        raise ValueError ("Timeout должен быть положительным")

    return f"Успех: retries={retries}, timeout={timeout}"


try:
    print(run_test(3, 5))


except ValueError as e:
    print(e)

try:
    print(run_test(17, 5))

except ValueError as e:
    print(e)

try:
    print(run_test(1, -9))
except ValueError as e:
    print(e)