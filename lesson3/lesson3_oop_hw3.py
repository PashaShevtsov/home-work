from lesson2_oop_hw import Developer
from lesson2_oop_hw import Recruiter

class Employee:

    def __init__(self, name: str, salary_day: int, days=0):
        self.name = name
        self.salary_day = salary_day
        self.days = days

    def work(self):
        return "I come to the office."

    def __lt__(self, other):
        return self.salary_day < other.salary_day

    def __le__(self, other):
        return self.salary_day <= other.salary_day

    def __gt__(self, other):
        return self.salary_day > other.salary_day

    def __ge__(self, other):
        return self.salary_day >= other.salary_day

    def __eq__(self, other):
        return self.salary_day == other.salary_day

    def __ne__(self, other):
        return self.salary_day != other.salary_day

    def check_salary(self, days):
        return self.salary_day * days


if __name__ == '__main__':
    rec1 = Recruiter("Artem",50,28)
    rec2 = Recruiter("Denis",75,22)
    dev1 = Developer("Pasha", 100, ["Python", "Java", "Pascal", "PHP"])
    dev2 = Developer("Nastya", 200, ["Python", "PHP", "C++"])


    print(rec1.work())
    print(dev1.work())
    print(rec1)
    print(rec2)
    print(dev1)
    print(dev2)
    print(rec1 > rec2)
    print(rec2 < dev1)
    print(rec1 >= dev2)
    print(rec1 == dev1)
    print(rec1.check_salary(28))
    print(rec1.check_salary(26))
    print(dev1.check_salary(30))
    print(dev2.check_salary(29))
    print(dev1 > dev2)
    print((dev1 + dev2).__dict__)
