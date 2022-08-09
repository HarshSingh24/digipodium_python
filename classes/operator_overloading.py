class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


if __name__ == "__main__":

    p1 = Person('raju', 39)
    p2 = Person('vijay', 20)
    p3 = Person('sujay', 30)


    if p1 > p3:
        print(f'{p1.name} is elder')
    person_list = [p1, p2, p3]
    person_list.sort()
    print(person_list)