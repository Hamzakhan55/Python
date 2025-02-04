class Person:
    def __init__(self, n, occ):
        self.name = n
        self.occupation = occ
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person("Khan", "developer")
b = Person("Hamza", "student")
a.info()
b.info()


#output

# Khan is a developer
# Hamza is a student