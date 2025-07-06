# 1. Homework 1: ToDo List Application

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} - {self.due_date} [{status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete(self):
        for task in self.tasks:
            if not task.completed:
                print(task)

todo = ToDoList()
todo.add_task(Task("Learn Python", "Variables and loops", "2025-07-01"))
todo.add_task(Task("Go Gym", "Chest day", "2025-07-02"))
todo.mark_complete("Learn Python")
todo.list_tasks()
print("--- Incomplete Tasks ---")
todo.list_incomplete()


# 2. Homework 2: Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all(self):
        for post in self.posts:
            print(post)

    def by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post)

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, old_title, new_title, new_content):
        for post in self.posts:
            if post.title == old_title:
                post.title = new_title
                post.content = new_content

    def latest_posts(self, count=3):
        for post in self.posts[-count:]:
            print(post)

blog = Blog()
blog.add_post(Post("Intro", "Welcome to my blog", "Salikh"))
blog.add_post(Post("Second", "Learning Python", "Salikh"))
blog.add_post(Post("Third", "Travel", "Ali"))
blog.list_all()
print("--- By Salikh ---")
blog.by_author("Salikh")
blog.edit_post("Second", "Python 101", "Updated content")
blog.delete_post("Third")
print("--- Latest ---")
blog.latest_posts()


# 3. Homework 3: Simple Banking System

class Account:
    def __init__(self, acc_num, holder, balance=0):
        self.acc_num = acc_num
        self.holder = holder
        self.balance = balance

    def __str__(self):
        return f"{self.holder} - {self.acc_num} - ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find(self, acc_num):
        for acc in self.accounts:
            if acc.acc_num == acc_num:
                return acc
        return None

    def check_balance(self, acc_num):
        acc = self.find(acc_num)
        if acc:
            print(f"Balance: ${acc.balance}")

    def deposit(self, acc_num, amount):
        acc = self.find(acc_num)
        if acc:
            acc.balance += amount

    def withdraw(self, acc_num, amount):
        acc = self.find(acc_num)
        if acc and acc.balance >= amount:
            acc.balance -= amount

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find(from_acc)
        receiver = self.find(to_acc)
        if sender and receiver and sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount

    def display_accounts(self):
        for acc in self.accounts:
            print(acc)

bank = Bank()
bank.add_account(Account("001", "Salikh", 500))
bank.add_account(Account("002", "Ali", 300))
bank.deposit("001", 200)
bank.withdraw("002", 100)
bank.transfer("001", "002", 150)
bank.display_accounts()
