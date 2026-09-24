
def print_report(test_cases, statuses):
    dict_print_report = dict(zip(test_cases, statuses))
    for key, value in dict_print_report.items():
        print(f"{key} - {value}")

        if "FAIL" in statuses:
            print("Test run failed")

        elif "FAIL" not in statuses:
            print("Test run completed successfully")




print_report(test_cases = ["Login", "Registration", "Checkout", "Logout"], statuses = ["PASS", "FAIL", "PASS", "SKIP"])

