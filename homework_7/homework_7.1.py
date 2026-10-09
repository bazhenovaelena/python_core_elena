

class CreditCard:
    balance_count = 0
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance


    def deposit(self, amount):
        print(f"Баланс пополнен на {amount} руб")
        self.__balance += amount



    def withdraw(self, amount):
        print(f"Со счета снято {amount} руб ")
        self.__balance -= amount

    def show_info(self):
        print(f"Баланс счета № {self.account_number} равен {self.__balance} руб ")

Ivan = CreditCard(123456, 1000)
Maria = CreditCard(654321, 5000)
Roman = CreditCard(98989765, 30000)

Ivan.deposit(20000)
Maria.deposit(5000)
Roman.withdraw(7000)

Ivan.show_info()
Maria.show_info()
Roman.show_info()

