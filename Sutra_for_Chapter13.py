# P158
# http://tinyurl.com/jj74o5rh

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

# P159
# http://tinyurl.com/jtz28ha

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def cange_data(self, index, n):
        self.nums[index] = n

data_one = Data(self, index, n):
data_one.nums[0] = 100
print(data_one.nums)


data_two = Data()
data_two.cange_data(0, 100)
print(data_two.nums)

# P160
# http://tinyurl.com/jkaorle

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._usafe = "unsafe"

    def public_method(self):
        # client が使っても良い
        pass # pass文は、文が必須な構文で何もしない場合に使う

    def _unsafe_method(self):
        # client は使うべきじゃない
        pass # pass文は、文が必須な構文で何もしない場合に使う

# P162
# http:tinyurl.com/hrxd7gn

print("Hello, World!")
print(200)
print(200.1)

# http://tinyurl.com/gnxq24x

typr("Hello, World!")
type(200)
type(200.1)

# このコードは例なので実行できません

# ポリモーフィズムなしでさまざまな形状を描画する場合
shapes = [trl, sql, crl]
for a_shape in shapes:
    if isinstance(a_shape, Triangle)
        a_shepe.draw_triangle()
    if isinstance(a_shape, Square)
        a_shepe.draw_square()
    if isinstance(a_shape, Circle)
        a_shepe.draw_circle()

# ポリモーフィズムを実装して描画する場合
shapes = [trl, swl, crl]
for a_shape in shapes():
    a_shape.draw()

# P164
# http://tinyurl.com/zrnqeo3
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


class Square(Shape):
    pass


a_square = Square(20, 20)
a_square.print_size()

# P166
# http://tinyurl.com/hwjdcy9

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len


a_square = Square(20, 20)
print(a_square.area())

# http://tinyurl.com/hy9m8ht

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 20)
a_square.print_size()

# P167
# http://tinyurl.com/zqg488n

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(selfm name):
        self.name = name

# P168
# http://tinyurl.com/zlzefd4
# 前のコードの続き

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog, mick")
print(stan.owner.name)