
def test(status):
    class InvalidTestStatusError(Exception):
        """Недопустимый статус"""
    try:
        valid_status = ["PASS", "FAIL", "SKIP"]
        if status not in valid_status:
            raise InvalidTestStatusError(f"Неизвестный статус теста: {status}")

        print(f"Статус {status} корректный")

    except InvalidTestStatusError as e:
        print(e)

test("WRONG")
test("PASS")
