class Person:
    name = ""
    occupation = ""
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
a.name = "Muhammad"
a.occupation = "Teacher"
b.name = "Hammad khan"
b.occupation = "Principal"
a.info()
b.info()

#output

# Muhammad is a Teacher
# Hammaad khan is Principal