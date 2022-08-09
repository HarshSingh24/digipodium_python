class Fruit:

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return f"{self.name} is {self.color}"

# every property and function is directly accessible from the class
# inheritance
class Mango(Fruit):

    def __init__(self, name, color, size, variety):
        super().__init__(name, color, size)
        self.variety = variety

if __name__ == "__main__":

    f = Fruit('watermelon', 'green', 'large')
    print(f)
    m = Mango('Mango', 'yellow', 'small', 'safeda')
    print(m)
    m2 = Mango('Mango','green', 'large', 'langda')
    print(m2)