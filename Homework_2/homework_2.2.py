password = "Python123"
attempts = [1,2,3,4]
for attempt in attempts:
   if attempt <= 3:
       password_input = input("Введите пароль:")


       if password_input == password:
           print("Авторизация прошла успешно")
           break
   if attempt > 3:
       print("Ваше устройство заблокировано")
