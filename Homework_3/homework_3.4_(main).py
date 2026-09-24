from collections import Counter
from utils import test_data as t


def user_list(amount):
    statistics = []
    for number in range(amount):
        user = t.generate_user()

        statistics.append(user["status"])
        print()

        print("Пользователь: ")
        for key, value in user.items():
            print(f"{key}: {value}")

    print()
    print("Общая статистика по статусам: ")
    stats_counter = Counter(statistics)
    print(stats_counter)


user_list(amount = int(input("Введите необходимое количество тестовых пользователей: ")))


