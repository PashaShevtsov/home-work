import traceback
from datetime import datetime


class EmailIsAlreadyTakenException(Exception):
    pass


class Employee:
    def __init__(self, name, salary_day, email):
        self.email = email
        self.validate()
        self.name = name
        self.salary_day = salary_day
        self.save_email()

    def save_email(self):
        with open('emails.txt', 'a+', ) as fp:
            fp.write(self.email.lower())

    def validate(self):
        with open('emails.txt') as fp:
            if self.email.lower() in fp.read():
                raise EmailIsAlreadyTakenException()


def main():
    emp = Employee("pasha", 100, 'Balotelli357951@gmail.com')
    emp1 = Employee("sasha", 150, 'lol357951@gmail.com')
    emp2 = Employee("joric", 200, 'nasdaQ222@gmail.com')


if __name__ == '__main__':
    try:
        main()
    except EmailIsAlreadyTakenException:
        with open('logs.txt', 'a+') as fp:
            fp.write(f"{datetime.now()} | {traceback.format_exc()}")

