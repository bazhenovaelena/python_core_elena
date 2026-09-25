test_input = int(input("Введите количество тестов: "))
total_tests = test_input
total_pass = []
total_fail = []
total_skip = []
for test in range (test_input):
    result = (input("Введите результаты тестов: "))

    if result == "FAIL":
        total_fail.append(test)

    elif result == "SKIP":
        total_skip.append(test)

    elif result == "PASS":
        total_pass.append(test)

    else:
        continue

if len(total_fail) > 0:
    print(f"Тестирование состояло из {total_tests} тестов. В результате мы получили {len(total_pass)} успешный(х) тест(a), {len(total_skip)} пропущенный(х) тест(a) и {len(total_fail)} проваленный(х) тест(a). Тестирование провалено.")

else:
    print(f"Тестирование состояло из {total_tests} тестов. В результате мы получили {len(total_pass)} успешный(х) тест(a), {len(total_skip)} пропущенный(х) тест(a) и {len(total_fail)} проваленный(х) тест(a). Тестирование завершено успешно.")


