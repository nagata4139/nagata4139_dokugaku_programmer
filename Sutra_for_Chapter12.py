# http://tinyurl.com/jv2rrl8

x = 2
y = 4
z = 8
xyz = x + y + z
xyz

# http://tinyurl.com/gldykam

pop = []
jpop = []

def collect_songs():
    song = "曲名を入力してください： "
    ask = "p か j のどちらかを入力してください。qで終わります： "

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)

        elif genre == "j":
            k = input(song)
            jpop.append(j)

        else:
            print("不正な値です。")

    print("pop songs: ", pop)
    print("pop songs: ", jpop)

collect_songs()

# P148
# http://tinuyurl.com/gu9jpco

a = 0

def increment():
    global a
    a += 1

# http://tinyurl.com/z27k2y1

def increment(a):
    return a + 1

# P150
# http]//tinyurl.com/zrmjape

class Orange:
    def __init__(self):
        print("Created!")

# P151
# http://tinyurl.com/hrf6cus

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

# http://tinyurl.com/jlc7pvk

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

orl = Orange(10, "dark orange")
print(orl)

# P152
# http:///tinyurl.com/grwzeo4

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")


orl = Orange(10, "dark orange")
print(orl.weight)
print(orl.color)

# P153