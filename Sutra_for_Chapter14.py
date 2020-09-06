# P171
# http://tinyurl.com/h7ypzmd

class Square:
    pass

print(Square)

# http://tinyurl.com/zmnf47e

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

# P172
# http://tinyurl.com/gu9unfc

class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

# P173
# http://tinyurl.com/ze8yr7s

class Lion:
    def __init__(self, name):
        self.name = name


lion = Lion("Dilbert")
print(lion)

# P174
# http://tinyurl.com/j5rocqm

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


lion = Lion("Dilbert")
print(lion)

# http://tinyurl.com/hlmhrwv

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)


print(x + y)

# P175
# http://tinyurl.com/gt28gwn

class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)


anothor_bob = Person()
print(bob is anothor_bob)

# P176
# http://tinyurl.com/jjettn2

x = 10
if x is None:
    print("x はNone :( ")
else:
    print("x はNoneじゃない :( ")

x = None
if x is None:
    print("x はNone")
    print("x はNoneじゃない :( ")