
def count_pass(tests):
    if len(tests) == 0:
        return 0
    if tests[0] == "PASS":
        return 1 + count_pass(tests[1:])
    else:
        return 0 + count_pass(tests[1:])


print(count_pass(["PASS", "FAIL", "SKIP", "PASS", "PASS", "PASS"]))