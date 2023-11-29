class Duck:

    def walk(self):
        print("waddle waddle")

    def swim(self):
        print("Water water")

    def quack(self):
        print("Quack Quack")

class Penguin:

    def walk(self):
        print(" Tap tap")

    def swim(self):
        print("dugu dugu")

    def quack(self):
        print("Well I dont, do I?")


def test_duck(obj):
    obj.walk()
    obj.swim()
    obj.quack()


if __name__ == "__main__":
    donald=Duck()
    pingo=Penguin()
    test_duck(donald)
    test_duck(pingo)
