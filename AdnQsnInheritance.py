class Hospital:
    def __init__(self,admin,doc,sis,dep):
        self.admin=admin
        self.doc=doc
        self.sis=sis
        self.dep=dep
    def getValues(self):
        print("Enter Hospital Record Details")
        self.admin=input("\nEnter the name of Admin: ")
        self.doc=input("\nEnter the name of Doctor: ")
        self.sis=input("\nEnter the name of Sister: ")
        self.dep=input("\nEnter the name of Department: ")

class Department(Hospital):
    def putValues(self):
        print("\nHospital Records\n*****************")
        print("Admin: ",self.admin)
        print("Doctor: ",self.doc)
        print("Sister: ",self.sis)
        print("Department: ",self.dep)
class Patient():
    def __init__(self, num, name, age, desease):
        self.num = num
        self.name = name
        self.age = age
        self.desease = desease
    def getDetails(self):
        print("Enter Patient Details")
        self.num = int(input("\nEnter the number : "))
        self.name = input("\nEnter the name of Patient: ")
        self.age = int(input("\nEnter the age : "))
        self.desease = input("\nEnter the name of Desease: ")
    def putDetails(self):
        print("\nPatient Details\n****************\n")
        print("Number: ", self.num)
        print("Patient: ", self.name)
        print("Age: ", self.age)
        print("Desease: ", self.desease)
dep1=Department(" "," "," "," ")
patient1=Patient(" "," "," "," ")
dep1.getValues()
dep1.putValues()
patient1.getDetails()
patient1.putDetails()