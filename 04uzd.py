class Human:

       def init(self, name, age, profession):
            self.name = name
            self.age = age
            self.profession = profession

        def description(self):
            print(f"My name is {self.name}, I'm {self.age} years old and I'm {self.profession}")

        def sport(self):
            print("{self.name} likes to do sports")

        def work(self):
            print("I would like to work in my profession -{self.profession} ")


tom = Human()
tom.init = ["Tom", 27, "pianist"]
# gita = Human("Gita", 35, "dentist")
# marttks = Human("Marks", 40, "driver")

tom.description()
# print(gita.sport())
# print(marks.work())
