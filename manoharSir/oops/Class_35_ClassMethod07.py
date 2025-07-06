


class Employee:
    company_name = "Tech Core"

    @classmethod
    def set_company_name(cls,name):  # with out touching the static variables, we can change with class method
        cls.company_name = name

print(Employee.company_name)
Employee.set_company_name("Inno Tech")
print(Employee.company_name)
