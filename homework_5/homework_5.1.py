from functools import reduce

tests = [{"name" : "Test_1", "status": "FAIL", "time" : 2},
         {"name" : "Test_2", "status": "PASS", "time" : 5},
         {"name" : "Test_3", "status": "PASS", "time" : 6},
         {"name" : "Test_4", "status": "FAIL", "time" : 10},
         {"name" : "Test_5", "status": "PASS", "time" : 15}
]

failed = list(filter(lambda x: x["status"] == "FAIL", tests))
failed_test_names = list(map(lambda x: x["name"], failed))
passed_tests = [x["name"] for x in tests if x["status"] == "PASS"]
times = [x["time"] for x in tests]
total_time = reduce(lambda x,y : x + y, times)


print("Количество упавших тестов: ", len(failed))
print("Список упавших тестов по названиям: ", failed_test_names)
print("Количество успешных тестов: ", len(passed_tests))
print("Список успешных тестов по названиям: ", passed_tests)
print("Общее время выполнения всех тестов: ", total_time, "мин")
