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

#　リスト2.11 fizzbuzz.pyの実行

#$ python3 fizzbuzz.py
#can't open file 'fizzbuzz.py': [Errno 2] No such file or directory

#　リスト2.12 for文と関数の実行

def fizzbuzz(num):
    return num

for num in range(1, 101):
    print(fizzbuzz(num))

#　リスト2.13 fizzbuzz.pyの実行

#$ python3 fizzbuzz.py
#1
#2
#3
#.
#.
#100

