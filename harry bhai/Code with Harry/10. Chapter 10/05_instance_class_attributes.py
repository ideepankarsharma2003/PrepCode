class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
harry.name='harry' # object attribute
harry.std = 12 # object attribute
print(f'The salary of harry is {harry.salary}-----> class attribute')
print(f'The name of harry is {harry.name}')
print(f'The class of harry is {harry.std}')
print(f'The salary of rajni is {rajni.salary} ---> class attribute')


# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 