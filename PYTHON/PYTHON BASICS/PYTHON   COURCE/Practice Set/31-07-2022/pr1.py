# OOps

class Employee:
    leaves = 20


sudarshan = Employee()
sim = Employee()

sudarshan.name = "Sudarshan"
sudarshan.sal = "10k"
sim.name = "Sim"

print(sudarshan.name,sim.name)
print(sudarshan.leaves)
print(sudarshan.__dict__)
print(Employee.leaves)

sim.leaves = 30
print(sim.leaves)
print(sudarshan.leaves)