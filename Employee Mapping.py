class Employee():
    def __init__(self, name, age, dept_name):
        self.name = name
        self.age = age
        self.dept_name = dept_name

class EmployeeFun():

    def employee_dict(self, employees):
        employee_dict = {}
        for emp in employees:
            # employee_dict[employee.dept_name] = employee.name, employee.age
            if emp.dept_name not in employee_dict:
                employee_dict[emp.dept_name] = []

            employee_dict[emp.dept_name] += [emp]
            # employee_dict[emp.dept_name].append(emp.age)

        return employee_dict

    def printEmpDict(self,dictv):
        print(dictv)
        for key,val in dictv.items():
            print(key)
            for obj in val:
                print(obj.name, obj.age, obj.dept_name)
            print("--------------------------------")
        return


employees = [Employee("Chitra", 30, "Development"), Employee("Karan", 28, "Development"),
            Employee("Prem", 29, "Marketing"), Employee("Varsha", 26, "Production"), Employee("Ed", 40, "Production"),
            Employee("Shiv", 35, "Testing")]

obj= EmployeeFun()
empdict=obj.employee_dict(employees)
obj.printEmpDict(empdict)


# for emp in emp_list:
#     print(emp.name, emp.age, emp.dept_name, sep=' | ')

# employee_table = {empl.name: empl for empl in emp_list}
# emp_dept_table = {empl.dept_name: empl for empl in emp_list}
#
# print(employee_table)

