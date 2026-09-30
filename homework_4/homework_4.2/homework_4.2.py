numbers = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n", "9\n", "10\n"]

file = open("even_numbers.txt", "w")
file.writelines(numbers[1::2])
file.close()

file = open("odd_numbers.txt", "w")
file.writelines(numbers[::2])
file.close()