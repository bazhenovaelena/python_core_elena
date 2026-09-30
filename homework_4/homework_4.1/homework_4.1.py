from traceback import print_tb

with open("int_numbers.txt", "r") as file:
    for line in file:
        total_lines = len(line)
        if total_lines > 3:
            print("Ошибка")
        else:
            print(line.split())

