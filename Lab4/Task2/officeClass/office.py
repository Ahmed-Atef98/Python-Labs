from employeeClass import Employee


class Office:
    employeesNumber = 0

    @classmethod
    def ChangeEmpsNum(cls, num: int):
        cls.employeesNumber = num

    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def GetAllEmployees(self):
        return self.employees

    def GetEmployee(self, eid: int):
        for employee in self.employees:
            if employee.eid == eid:
                return employee
        return None

    def Hire(self, cls, employee: Employee):
        self.employees.append(employee)
        cls.ChangeEmpsNum(cls.employeesNumber + 1)

    def Fire(self, cls, eid: int):
        for i in range(0, len(self.employees)):
            if self.employees[i].eid == eid:
                del self.employees[i]
                cls.ChangeEmpsNum(cls.employeesNumber - 1)

    def Deduct(self, eid: int, deduction: int):
        if isinstance(deduction, int):
            for i in range(0, len(self.employees)):
                if self.employees[i].eid == eid:
                    self.employees[i].salary -= deduction
        else:
            print("Deduction must be integer")

    def Reward(self, eid: int, reward: int):
        if isinstance(reward, int):
            for i in range(0, len(self.employees)):
                if self.employees[i].eid == eid:
                    self.employees[i].salary += reward
        else:
            print("Reward must be integer")

    @staticmethod
    def CalculateLateness(targetHour: int, moveHour: int, distance: int, velocity: int):
        empHour = moveHour + distance/velocity
        if empHour > targetHour:
            return True
        else:
            return False

    def CheckLateness(self, eid: int ,targetHour: int , moveHour: int):
        for i in range(0, len(self.employees)):
            if self.employees[i].eid == eid:
                if Office.CalculateLateness(targetHour, moveHour, self.employees[i].distanceToWork, self.employees[i].car.velocity):
                    self.employees[i].salary -= 10
                else:
                    self.employees[i].salary += 10