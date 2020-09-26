# リスト1.1 Pythonのバージョンを確認
#$ python3 -V
#Python 3.6.7

# リスト1.2 Pythonのバージョンを確認

#$ python3 -V
#Python 3.6.5

# リスト2.1 Pythonインタープリタの起動

#$ python3
#Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 03:02:14)
#[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.

# リスト2.2 四則演算と代入
print(2 + 2)

print(3 - 8)

print(6 * 9)

print(8 / 2)

print(5 % 2)

width = 60
height = 90
print(width * height)

# リスト2.3 文字列型

print("Hello,World!")

print("Monty Python's Flying Circus")

# リスト2.4 リスト

print(["Hello",3])

# リスト2.5 コメントの書き方

# ここはコメント文
a = 1 # コードの右側にも書ける

# リスト2.6 関数定義と呼び出し

def add(a,b):
    return a + b

print(add(1,3))

# リスト2.7 組み込み関数round

print(round(10.4))

# リスト2.8 FizzBuzzの15までの回答

#1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

# リスト2.9 fizzbuzz.py

def fizzbuzz(num):
    return  num

print(fizzbuzz(4))

# リスト2.10 fizzbuzz.pyの実行

#$ python3 fizzbuzz.py
#4

# リスト2.11 fizzbuzz.pyの実行

#$ python3 fizzbuzz.py
#can't open file 'fizzbuzz.py': [Errno 2] No such file or directory

# リスト2.12 for文と関数の実行

def fizzbuzz(num):
    return num

for num in range(1,101):
    print(fizzbuzz(num))

# リスト2.13 fizzbuzz.pyの実行

#$ python3 fizzbuzz.py
#1
#2
#3
#.
#.
#100

# リスト2.14 fizzbuzz関数を完成させる

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

for num in range(1,101):
    print(fizzbuzz(num))

# リスト2.15 完成したfizzbuzz.pyの実行

#$ python3 fizzbuzz.py
#1
#2
#Fizz
#4
#Buzz
#Fizz
#7
#8
#Fizz
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz
#.
#.
#Buzz

# リスト2.16 文字列とリストとそれらの型

n1 = 100
s1 = "hello"
l1 = [1, 2, 3]
print(type(n1))
print(type(s1))
print(type(l1))
print(isinstance(n1, int))
print(isinstance(s1, str))
print(isinstance(l1, list))

import collections.abc
print(isinstance(s1, collections.abc.Sequence))
print(isinstance(l1, collections.abc.Sequence))

# リスト 3.1 整数型)

print(2 + 2)

print(3 - 8)

print(6 * 9)

print(8 / 2)

print(5 % 2)

print(5 ** 2
)

# リスト 3.2 整数型同士の商)

print(10 / 3)

print(10 / 4)

print(-10 / 4)

# リスト 3.3 //での割り算)

print(10 // 3)

print(10 // 4)

print(-10 // 4)

# リスト 3.4 浮動小数点型)

print(5.0)

print(5.0 + 5.2)

print(10.2 + 8)

# リスト 3.5 文字列型)

print('Hello,world')

print("Hello,world")

# リスト 3.6 文字列中のエスケープ)

print("I\'m Hiroki")

print("Hello\nworld")

# リスト 3.7 シングルクォートを含む文字列)

print("I'm Hiroki")

# リスト 3.8 三重クォート)

""" foo
... bar
... baz
... """

# リスト 3.9 文字列の結合)

print("Mt." + "Fuji")

# リスト 3.10 文字列の繰り返し)

print("spam" * 5)

# リスト 3.11 文字列から1文字取り出し)

print("python"[1])

# リスト 3.12 文字列のスライス)

print("python"[2:5])

# リスト 3.13 先頭末尾からのスライス)

print("python"[:3])

print("python"[4:])

# リスト 3.14 文字列長の取得)

print(len("python"))

# リスト 3.15 文字列中にある文字列が存在するかのチェック)

print("t" in "python")

print("k" in "python")

print("th" in "python")

# リスト 3.16 文字列の分割)

print("pain-au-chocolat".split("-"))

# リスト 3.17 文字列の結合

print("-".join(["pain", "de", "campagne"]))