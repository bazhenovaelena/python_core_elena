

def get_test_statistics(results):
    res = results.split()
    passes = []
    fails = []
    skips = []

    for status in res:
        if status == "PASS":
            passes.append(status)

        elif status == "FAIL":
            fails.append(status)


        elif status == "SKIP":
            skips.append(status)

    status_options = ["PASS", "FAIL", "SKIP"]

    status_count = list()
    status_count.append(len(passes))
    status_count.append(len(fails))
    status_count.append(len(skips))

    pass_percentage = int(len(passes)) / len(res) * 100
    pass_percentage = round(pass_percentage, 1)



    print(f'Total test amount: {len(res)}')
    dict_statistics= dict(zip(status_options, status_count))
    for key, value in dict_statistics.items():
        print(f'{key}: {value}')
    print(f"Success rate: {pass_percentage}%")


get_test_statistics(results = input("Enter test status: "))



