from lesson2_oop_hw import Employee


class Recruiter(Employee):
    def __init__(self, name: str, salary_day: int, days):
        super().__init__(name, salary_day, days)

    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return f"{__class__.__name__} : {self.name}"


class Developer(Employee):
    def __init__(self, name: str, salary_day: int,  tech_stack: list):
        super().__init__(name, salary_day,)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start to coding"

    def __str__(self):
        return f"{__class__.__name__} : {self.name}"

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __add__(self, other):
        return Developer(name=self.name + " " + other.name, salary_day=max(self.salary_day, other.salary_day), tech_stack=list(self.tech_stack + other.tech_stack))


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
