class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}"

    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, "
            f"{repr(self.age)}, "
            f"{repr(self.position)}, "
            f"{repr(self.salary)})"
        )

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be positive")


employee1 = Employee("John", 25, "Software Developer", 5000)
employee2 = Employee("Mary", 23, "Data Scientist", 6000)

print(employee1)
print(employee2)