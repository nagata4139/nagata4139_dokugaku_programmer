# P125
# http://tinyurl.com/hkqfkar

import os
os.path.join("Users","bob","st.txt")

# P126
# http://tinyurl.com/zfgczj5

st = open("st.txt","w")
st.write("Hi from Python!")
st.close()

st = open("st.txt","w",encoding="utf-8")
st.write("Pythonからこんにちは！")
st.close

# P127
# http://tinyurl.com/jt9guu2

with open("st.txt","w") as f:
    f.write("Hi from Python!")

# P128
# http://tinyurl.com/hmuamr7

# 前の節で作成したファイルを読み込みます

with open("st.txt","r") as f:
    print(f.read())

with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())

# http://tinyurl.com/hkzhxdz

my_list = []

with open("st.txt","r") as f:
    my_list.append(f.read())

print(my_list)

# P130
# http://tinyurl.com/go9wepf

import csv

with open("st.csv","w",newline="") as f
    w = csv.writer(f,delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])

# http://tinyurl.com/gvcdgxf

# ここで開くファイルは、
# 前のコード例を実行して作られます。

import csv

with open("st.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))