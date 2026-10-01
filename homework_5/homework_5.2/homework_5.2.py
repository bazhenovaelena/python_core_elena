import json


def read_users():
    required_fields = ["User", "Login", "Password", "Auth"]
    try:
        with open("../homework_5.2/Users.json", "r") as file:
            all_users = json.load(file)
            for user in all_users:
                print()
                missing_fields = [field for field in required_fields if field not in user]
                if missing_fields:
                    print("Отсутствует обязательное поле")

                for key, value in user.items():
                        print(f"{key}: {value}")

    except FileNotFoundError as e:
        print("Файл 'Users.json' не найден")
    except ValueError as e:
        print("Файл невозможно прочитать как JSON")

read_users()

