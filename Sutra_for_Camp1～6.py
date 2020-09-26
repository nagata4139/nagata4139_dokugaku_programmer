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
#Type "help","copyright","credits" or "license" for more information.

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

print("-".join(["pain","de","campagne"]))

# リスト 4.1 リストの定義

print(["spam","egg", 0.5])

# リスト 4.2 リストの基本的な使い方

print(["spam","ham"] + ["egg"])              # リストの結合

print(["spam"] * 5)                           # リストの繰り返し

print(["spam","ham","egg"][0] )             # リストの0番目を取得する

print(["spam","ham","egg"][1:])             # リストのスライス(1番目以降)

print(len(["spam","ham","egg"]))            # リストの長さ

print("ham" in ["spam","ham","egg"])        # リストに特定の文字列が含まれるか

# リスト 4.3 for文とリスト

for animal in ["cat","dog","snake"]:
    print(animal)

# リスト 4.4 リストへの要素追加

animals = ["cat","dog","snake"]
animals.append("elephant")
print(animals)

# リスト 4.5 一般的なfor文
ret = []
for animal in animals:
    ret.append(len(animal))
print(ret)

# リスト 4.6 リスト内包表記

print([len(animal) for animal in animals])

# リスト 4.7 シーケンス型から複数変数への代入

dog, cat = ["dog","cat"]
print(dog)
print(cat)

# リスト 4.8 タプルの定義

print(("spam","ham", 4))

# リスト 4.9 タプルの基本的な使い方

print(("spam","ham") + ("egg",))             # タプルの結合

print(("spam",) * 5)                          # タプルの繰り返し

print(("spam","ham","egg")[0])              # タプルの0番目を取得する

print(("spam","ham","egg")[1:])             # タプルのスライス(1番目以降)

print(len(("spam","ham","egg")))            # タプルの長さ

print("ham" in ("spam","ham","egg"))        # タプルに特定の文字列が含まれるか

# リスト 4.10 1要素のタプル

print(("spam",))

print(("spam"))

# リスト 4.11 括弧を省略したタプル

print("dog","cat")

# リスト 4.12 タプルを返す関数
def head_splitter(seq):
    return seq[0], seq[1:]

head, tail = head_splitter(["head","body","tail"])
print(head)
print(tail)

# リスト 4.13 要素数の多いタプルを返す関数

def bad_implementation():
    return "username","user_password","user_id","user_permission1","user_permission2"

username, user_password, user_id, user_permission1, user_permission2 = bad_implementation()

# リスト 4.14 辞書

user_info = {"user_name": "taro","last_name": "Yamada"}
print(user_info)

# リスト 4.15 辞書からの値の取り出し

print(user_info["user_name"])

# リスト 4.16 辞書への値の設定

user_info["first_name"] = "Taro"
print(user_info)

# リスト 4.17 辞書のin

print("user_name" in user_info)
print("bio" in user_info)

# リスト 4.18 存在しないキーの参照

#user_info["bio"]
#Traceback (most recent call last):
#  File "C:/Users/M.Nagata/PycharmProjects/pythonProject/nagata4139_dokugaku_programmer/Sutra_for_Camp1～6.py", line 363, in <module>
#    user_info["bio"]
#KeyError: 'bio'

# リスト 4.19 存在しないキーへのget

print(user_info.get("user_name"))
bio = user_info.get("bio")
print(bio)

# リスト 4.20 デフォルト値付きのget

print(user_info.get("bio",""))

# リスト 4.21 辞書を使用したfor文

user_info = {"user_name": "taro","last_name": "Yamada"}
for key in user_info:
    print(key)
    print(user_info[key])

# リスト 4.22 辞書内のすべてのキーと値を取得

d = {"foo": "spam","bar": "ham"}
print(d.items())

# リスト 4.23 for文で辞書のキーと値を使う

d = {"foo": "spam","bar": "ham"}
for key, value in d.items():
    print(key, value)

# リスト 4.24 集合の定義

print({"spam","ham"})
print({"spam","spam","spam"})

# リスト 4.25 集合への要素の追加

unique_users = {"dog","cat"}
unique_users.add("snake")
print(unique_users)

# リスト 4.26 集合によるユニーク数管理

print(len(unique_users))
unique_users.add("snake")
unique_users.add("snake")
unique_users.add("snake")
print(len(unique_users))

# リスト 4.27 2集合の積

allowed_permissions = {"edit","view"}
requested_permissions = {"view","delete"}
print(allowed_permissions & requested_permissions)

# リスト 4.28 2つの集合の和

editor = {"edit","comment"}
reviewer = {"comment","approve"}
print(editor | reviewer)

# リスト 5.1 ファイルを開く

f = open("pycamp.txt","w", encoding="utf-8")
f

# リスト 5.2 ファイルへ書き込み

f.write("Hello")
f.write(" Python\n")  # 改行を書き込むには \n を指定する
f.write("こんにちはPython\n")  # 日本語も書き込み可能

# リスト 5.4 ファイルを閉じる

f.close()

# リスト 5.5 ファイル内容の読み込み

f = open("pycamp.txt","r", encoding="utf-8")
f
txt = f.read()
print(txt)
f.close()

# リスト 5.5 ファイル内容の読み込み

f = open("pycamp.txt", "r", encoding="utf-8")
f
txt = f.read()
print(txt)
f.close()

# リスト 5.6 第2引数を省略してファイルを開く

f = open("pycamp.txt", encoding="utf-8")
f

# with文でのファイルオープン
with open("pycamp.txt", encoding="utf-8") as f:
    txt = f.read()

print(txt)

# リスト 5.8 追記モードでファイルを開く

f = open("pycamp.txt", "a", encoding="utf-8")
f.write("こんにちは世界\n")


# リスト 5.10 add()、sub()関数の定義（calc.py）

#def add(a, b):
#    return a + b


#def sub(a, b):
#    return a - b


# リスト 5.11 calcのインポート

import calc

# リスト 5.12 別モジュールの関数を利用

print(calc.add(1, 2))

# リスト 5.13 関数のインポート

from calc import add

print(add(1, 2))

# リスト 5.14 インポート対象に別名をつける¶

import calc as c

print(c.add(1, 2))

# リスト 5.15 複数の対象をインポート

from calc import add, sub

print(add(1, 2))
print(sub(2, 1))

# リスト 5.16 括弧を使った複数のインポート
from calc import (
    add,
    sub,
)