import json
from functools import reduce


def statistics():
    try:
        with open("tests.json") as file:
            data = json.load(file)
            total_tests = len(data)
            passed_tests = list(filter(lambda x : x["status"] == "PASS", data))
            failed_tests = list(filter(lambda x : x["status"] == "FAIL", data))
            skipped_tests = list(filter(lambda x : x["status"] == "SKIP", data))
            failed_test_names = [x["name"] for x in failed_tests]
            longest_test = max(data, key=lambda x: x["time"])
            times = [x["time"] for x in data]
            total_time = reduce(lambda x,y : x + y, times)

            required_fields = ["name", "status", "time"]

            for x in data:
                missing_fields = [field for field in required_fields if field not in x]
                if missing_fields:
                    print("Отсутствует обязательное поле")

            keys = ["Общее количество тестов: ", "Количество успешных тестов: ", "Количество проваленных тестов: ",
                    "Количество пропущенных тестов: ", "Наименования упавших тестов: ", "Самый длительный тест: ",
                    "Общее время тестов: "]
            values = [total_tests, len(passed_tests), len(failed_tests), len(skipped_tests), failed_test_names, longest_test["time"], total_time]

            report_dict = dict(zip(keys, values))
            for key,value in report_dict.items():
                print(f"{key}: {value}")


    except FileNotFoundError as e:
        print("Файл 'tests.json' не найден")
    except ValueError as e:
        print("Файл невозможно прочитать как JSON")

    with open("report.json", "w", encoding = 'utf-8') as file:
        json.dump(report_dict, file, indent = 4, ensure_ascii = False)

statistics()



