import time as t

i = input("ENTER YOUR NAME!!")
print()
print("Hello", i)
print()
t.sleep(1)
print("Welcome to my quiz!!")
print()
t.sleep(1)
print("You will get 5 questions to answer!!")
print()
t.sleep(1)
print("You will get 2 points if you answer correctly")
print()
t.sleep(1)
print\
    ("There will be 4 options for each question,you will have to answer the correct one!!")
print()
t.sleep(1)
n = input("Type yes if you are ready!!\n")
if n == "yes" or n == "YES":
    t.sleep(1)
    print("okk lets go..!!")
    print()
else:
    print("Game over!!")
    exit()
z = 0
print("Here is your first question!!")
print()
a = input("""Q- Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom\n""")
print()
if a == "C" or a == "c":
    print("Awesome!!")
    print()
    z += 2
    t.sleep(1)
    print("You scored", z, "points")
    print()
else:
    print("Ooops...Not correct!!")
    print()
    t.sleep(1)
    print("The correct option is C")
    print()
print("Now its time for the next question!!")
print()
b = input("""Q-Which type of Programming does Python support?
a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned\n""")
print()
if b == "D" or b == "d":
    print("Excellent!!")
    print()
    z += 2
    t.sleep(1)
    print("You scored", z, "points")
    print()
else:
    print("Ooops...Not correct!!")
    print()
    t.sleep(1)
    print("The correct option is d")
    print()
print("Now its time for the next question!!")
print()
t.sleep(2)
c = input("""Q- What will be the output of the following Python code?

i = 1
while True:
    if i%3 == 0:
        break
    print(i)

    i + = 1
a) 1 2 3
b) error
c) 1 2
d) none of the mentioned\n""")
print()
if c == "B" or c == "b":
    print("You are Genius!!")
    print()
    z += 2
    t.sleep(1)
    print("You scored", z, "points")
    print()
else:
    print("Ooops...Not correct!!")
    print()
    t.sleep(1)
    print("The correct option is B")
    print()
print("Now its time for the next question!!")
print()
d = input("""Q- What does pip stand for python?
a) Pip Installs Python
b) Pip Installs Packages
c) Preferred Installer Program
d) All of the mentioned\n""")
print()
if d == "C" or d == "c":
    print("Great!!")
    print()
    z += 2
    t.sleep(1)
    print("You scored", z, "points")
    print()
else:
    print("Ooops...Not correct!!")
    print()
    t.sleep(1)
    print("The correct option is c")
    print()
print("Now its time for the next question!!")
print()
e = input("""Q- Which of the following character is used to give single-line comments in Python?
a) //
b) #
c) !
d) /*\n""")
print()
if e == "b" or e == "B":
    print("OP..!!")
    print()
    print("Fantastic")
    print()
    z += 2
    t.sleep(1)
    print("You scored", z, "points")
    print()
    t.sleep(1)
    print("Game over!!")
    print()
    print("Your total score =", z, "Out of 10")
else:
    t.sleep(1)
    print("Ooops...Not correct!!")
    print()
    t.sleep(1)
    print("The correct option is B")
    t.sleep(1)
    print("Game over!!")
    print()
    print("Your total score =", z, "Out of 10")