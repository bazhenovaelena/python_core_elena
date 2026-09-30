file = open("float_numbers.txt", "r")

squared_lines = []
for line in file:
    line = line.strip()
    if line:
        num = float(line)
        squared_lines.append(str(num * num) + "\n")
file.close()


file = open("float_numbers.txt", "w")
file.writelines(squared_lines)
file.close()