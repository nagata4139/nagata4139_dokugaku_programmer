# P105
# http://tinyurl.com/jya6kpm

name = "Ted"
for character in name:
    print(character)

# http://tinyurl.com/zeftpq8

shows  = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)

# http://tinyurl.com/gpr5a6e

coms = ("A. Development", "Friends", "Always Sunny")
for show in coms:
    print(show)

# P106
# http://tinyurl.com/jk7do9b

people = {"G. Bluth II": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny",
          }

for character in people:
    print(character)

# http://tinyurl.com/j8wvp8c

tv = ["GOT", "Narcos", "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

# P107
# http://tinyurl.com/z45g63j

tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

# http://tinyurl.com/zcvgklh

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

# P108
# http://tinyurl.com/hh5t8rw

for i in range(1, 11):
    print(i)

# P109
# http://tinyurl.com/j2gwcy

x = 10
while x > 0:
    print("{}".format(x))
    x -= 1
print("Happy New Year!")

# P110
# http://tinyurl.com/hcwvfk8

# while True:
#     print("Hello World!")

# http://tinyurl.com/zrdh88c

for i in range(0, 100):
    print(i)

# http://tinyurl.com/zhxf3uk


for i in range(0, 100):
    print(i)
    break

# http://tinyurl.com/jmak8tr

qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

# P112
# http://tinyurl.com/hflun4p

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# http://tinyurl.com/gp7forl

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# P113
# http://tinyurl.com/gqjxjtq

for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

# P114

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)