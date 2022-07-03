from tkinter import *
from tkinter import messagebox
from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract command classes will create the operations"""

    @abstractmethod
    def execute(self) -> None:
        pass

class Withdraw(Command):
    """Account withdraw button class"""

    def __init__(self, receiver, value):
        self._receiver = receiver
        self._value = value

    def execute(self):
        self._receiver.withdraw(self._value)

class Deposit(Command):
    """Account deposit button class"""

    def __init__(self, receiver, value):
        self._receiver = receiver
        self._value = value

    def execute(self):
        self._receiver.deposit(self._value)

class Statement(Command):
    """Account bank statement button class"""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        return self._receiver.statement()


class Invoker:
    """Invoker class """

    _withdraw = Withdraw
    _deposit = Deposit
    _statement = Statement

    def withdraw(self, reciever, value):
        self._withdraw(reciever, value).execute()

    def deposit(self, reciever, value):
        self._deposit(reciever, value).execute()

    def statement(self, reciever):
        return self._statement(reciever).execute()


class Account:
    """Bank account class"""

    def __init__(self, name):
        self._name = name
        self._value = 0
        self._bank_statement = []
    
    def deposit(self, value):
        self._value += value
        self._bank_statement.append("deposit : " + str(value))
    
    def withdraw(self, value):
        self._value -= value
        self._bank_statement.append("withdraw : " + str(value))
    
    def statement(self):
        return self._bank_statement

class Screen:
    """Tkinter GUI class"""

    def __init__(self, master, account):
        person = account
        frame = Frame(master)
        frame.grid(column = 4, row = 4)
        
        self.wlcmsg = Label(frame, text = "Welcome: " + person._name, fg = "black")
        self.wlcmsg.grid(column = 1, row = 0)

        self.accountvalue = Label(frame, text = "$" + str(person._value), fg = "green")
        self.accountvalue.grid(column = 1, row = 1)

        self.btnentry = Entry(frame)
        self.btnentry.insert(0, "0")
        self.btnentry.grid(column = 1, row = 2)

        self.btndeposit = Button(frame, text = "Deposit", fg = "black", command = self.depositaccount)
        self.btndeposit.grid(column = 0, row = 2)

        self.btnwithdraw = Button(frame, text = "Withdraw", fg = "black", command = self.withdrawaccount)
        self.btnwithdraw.grid(column = 2, row = 2)

        self.statement = Button(frame, text = "Statement", fg = "black", command = self.statementaccount)
        self.statement.grid(column = 0, row = 3)

        self.btnquit = Button(frame, text = "Quit", fg = "red", command = frame.quit)
        self.btnquit.grid(column = 2, row = 3)

    def depositaccount(self):
        invoker.deposit(MyAccount, float(self.btnentry.get()))
        self.accountvalue.config(text = "$" + str(MyAccount._value))

    def withdrawaccount(self):
        invoker.withdraw(MyAccount, float(self.btnentry.get()))
        self.accountvalue.config(text = "$" + str(MyAccount._value))

    def statementaccount(self):
        messagebox.showinfo("Bank Statement", invoker.statement(MyAccount))

if __name__ == "__main__":
    """Client code"""

    MyAccount = Account("User")
    invoker = Invoker()
    root = Tk()
    app = Screen(root, MyAccount)
    root.mainloop()