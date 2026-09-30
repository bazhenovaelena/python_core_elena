with open("file_1.txt", "r") as file:
    file_1 = file.read()

with open("file_2.txt", "r") as file:
    file_2 = file.read()

with open("file_1.txt", "w") as file:
    file.write(file_2)

with open("file_2.txt", "w") as file:
    file.write(file_1)
