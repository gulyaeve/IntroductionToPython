class Human:
    def __init__(self, age: int, name):
        self.age = age
        self.name = name
    
    def increase_age(self, years: int = 1):
        self.age += years

    # def __str__(self):
    #     return f"Human name: {self.name}, age: {self.age}."

    def __int__(self):
        return self.age

    def __float__(self):
        return float(self.age)
    
    def holidays(self):
        raise NotImplementedError()

    def __repr__(self):
        return f"Human(age={self.age}, name='{self.name}')"

    @property
    def double_age(self):
        return self.age * 2
        

class Student(Human):
    def __init__(self, age, name, student_id):
        Human.__init__(self, age, name)
        self.student_id = student_id
        
    def student_info(self):
        info = f"Student_NAME: {self.name}\nStudent_AGE: {self.age}\nStudent_ID: {self.student_id}"
        return info

    def __str__(self):
        return self.holidays()

    @staticmethod
    def secret_method(name: str):
        return name

    # def holidays(self):
    #     return self.student_info()
        

if __name__ == "__main__":
    kid = Human(7, "Petya")
    print(kid.double_age)

    # str_kid = "<__main__.Human object at 0x7f2542417010>"
    kid_2 = eval(repr(kid))
    print(type(kid_2))

    # student_1 = Student(18, "Vasya", 123)
    # student_1.student_info()
    # student_1.increase_age()
    # student_1.student_info()
    # print(student_1.secret_method("123"))
    # print(str(kid.holidays))
