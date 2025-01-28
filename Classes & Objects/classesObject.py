class Person:
    name = "Hamza Khan"
    occupation = "Student"
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
a.name = "Muhammad"
a.occupation = "Teacher"
a.info()

#output

# Muhammad is a Teacher