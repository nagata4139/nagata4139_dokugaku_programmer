import this

# http://tinyurl.com/z9pephe

#$ export GREP_OPTIONS="--color=always"

# http://tinyurl.com/jgh3x4c

#$ grep Beautiful zen.txt

# http://tinyurl.com/j3z6t2r

#$ grep beautiful zen.txt

# http://tinyurl.com/zchmrdq

#$ grep -i beautiful zen.txt

# http://tinyurl.com/zfcdnmx

#$ grep -o beautiful zen.txt

# http://tinyurl.com/z9q2286

import re

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)

# http://tinyurl.com/jzeonne

import re

l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

# http://tinyurl.com/gleyzan

#$ grep ^If zen.txt

# http://tinyurl.com/zkvpc2r

#$ grep idea.$ zen.txt

# http://tinyurl.com/zntqzc9

import re

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

# http://tinyurl.com/jf9quz

#$ echo Two too. | grep -i t[ow]o

# http://tinyurl.com/hg9sw3u

import re

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

# http://tinyurl.com/gm8o6gb

#$ echo 123 hi 34 hello. | grep [[:digit]]

# http://tinyurl.com/z3hr4q8

import re

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

# http://tinyurl.com/j8vbwq8

#$ echo two twoo not too. | grep -o two*

# http://tinyurl.com/h5x6cal

#$ echo __hello__there | grep -o __.*__

# http://tinyurl.com/j9v9t24

#$ echo __hi__bye__hi__there | grep -o __.*__

# http://tinyurl.com/j399sq9

import re

t = "__one__ __two__ __three__"
found = re.findall("__.*?__",t)
for match in found:
    print(match)

# http://tinyurl.com/ze6oyua

import re
text = """キリンは大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ の中で一番背が高いですが、科学者たちは
そのような長い __体の一部__ をどうやって獲得したのか説明できません。
キリンの身長は __数値__ __単位__ 近くあり、
その高さのほとんどは脚と __体の一部__ によるものです。
"""

def mad_libs(mls):
    """
    :param mls:文字列で、ユーザーに入力してもらいたい単語(=ヒント)
    の部分は後ろを2つのアンダースコアで挟んでください。
    ヒントの単語にはアンダースコアを含めないでください。
    __hint_hint__ はだめです。 __hint__ はOKです。
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
            print("\n")
            mls = mls.replace("\n", "")
            print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)