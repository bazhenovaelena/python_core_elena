for number in range(1, 31):
   if number % 3 == 0:
       print("Bug")
   elif number % 5 == 0:
       print("Test")
   elif number % 3 == 0 and number % 5 == 0:
       print("BugTest")
   else:
       print(number)
