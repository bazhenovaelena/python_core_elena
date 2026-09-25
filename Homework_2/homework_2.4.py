secret = 37
amount = []
for x in range(0,100000):
   user_input = int(input("Введите число: "))
   if user_input > secret:
       print("Ваше число больше загаданного")
       amount.append(user_input)
   elif user_input < secret:
       print("Ваше число меньше загаданного")
       amount.append(user_input)
       count_amount = len(amount)
   if user_input == secret:
       amount.append(user_input)
       count_amount = len(amount)
       print(f"Это успех! Вы угадали число с {count_amount} раза")
       break
