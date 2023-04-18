class Human:

    def name(self):
        print("I have a nice name!")

    def age(self):
        print("I am old")

    def country(self):
        print("I'm from beautiful country.")


class Student(Human):

    def lecture(self):
        print("I have a lecture today!")

    def hobbies(self):
        print("I have a hobbies!")

    def books(self):
        print("I need to read books!")


class Car(Human):

    def speed(self):
        print("This is a speed!")

    def color(self):
        print("The color is ...")

    def brand(self):
        print("I like ..... brand.")


Markus = Student()
Gustavs = Human()
Audi = Car()


Markus.lecture()
Gustavs.name()
Audi.color()
Audi.country()
Markus.books()
Markus.name()
