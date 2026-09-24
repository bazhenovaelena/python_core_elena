import random


def report(amount):
    tests = ["test_login",
         "test_logout",
         "test_registration",
         "test_profile",
         "test_payment",
         "test_search"]

    status = ['PASS', 'FAIL', 'SKIP']

    if amount > len(tests):
        print("Ошибка. Вы ввели недопустимое количество тестов.")

    elif amount <= len(tests):
        unique_tests = random.sample(tests, amount)
        random_status = random.choices (status, k = amount )

        dict_report = dict(zip(unique_tests, random_status))
        for key, value in dict_report.items():
            print(f"{key} : {value}")

report(amount = int(input("Введите количество тестов: ")))

