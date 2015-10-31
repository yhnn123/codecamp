# 1

print "Welcom to Python!"
print "hi"



# 2

my_variable = 10

print my_variable



# 3

# 앞서 설명 란에서 얘기한 변수와 각 변수의 값들을 지정하세요!

my_int = 7
my_float = 1.23
my_bool = True

print my_int
print my_float
print my_bool



# 4

# 아래에 변수 my_int의 값은 7로 지정되어 있습니다.
# 지정된 값을 3으로 변경하고 결과를 출력하려면 어떻게 해야할까요?

my_int = 7

# 여덟 번째 줄에서 변수 my_int의 값을 3 으로 변경하세요!

my_int = 3

# 변수 my_int의 값을 console에 출력하는 코드는 아래와 같습니다:
# 여기서 사용된 print 키워드는 이후 더 자세히 다룰 예정입니다!

print my_int



# 5

def spam():
eggs = 12
return eggs
        
print spam()



# 6

def spam():
    eggs = 12
    return eggs
        
print spam()



# 7

spam = True
eggs = False



# 8 

mysterious_variable = 42 # 주석이당



# 9

""" 주석이당
주석이당
주석이당
주
석
주
석 """



# 10

# 세 번째 줄에서 변수 count_to의 값으로 1 더하기 2를 지정하세요!

count_to = 1+2

print count_to



# 11

# 세 번째 줄에서 거듭제곱을 이용하여 변수 eggs의 값을 100으로 지정하세요!

eggs = 10 ** 2

print eggs



# 12

# 세 번째 줄에서 모듈로 연산을 이용하여 변수 spam의 값을 1로 지정하세요!

spam = 5 % 2

print spam



# 13

# 주석을 작성하래 ㅋㅋ

monty = True
python = 1.234
monty_python = python ** 2

print monty
print python
print monty_python



# 14

# 세 번째 줄에 변수 variable의 값으로 44.50을 지정하세요!

meal = 44.50 



# 15

meal = 44.50

tax = 0.0675



# 16

# 거의 다 됐습니다! 다섯 번째 줄에 변수 tip을 생성하세요.

meal = 44.50
tax = 0.0675
tip = 0.15



# 17

# Reassign meal on line 7!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + (meal * tax)



# 18

# 여덟 번째 줄에 변수 total을 생성하세요!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)



# 19

# 세 번째 줄에 변수 brain을 생성하세요!

brian = "언제나 삶의 긍정적인 면을 살피세요!"



# 20

# 각 줄마다 하나씩, 변수들을 생성하고 값을 지정하세요!

caesar = "Graham"
praline = "John"
viking = "Teresa"

# 변수들은 이 줄 위에 작성되어야 합니다.

print caesar
print praline
print viking


# 21

# 아래의 문자열에 문제가 있습니다. 백슬래쉬를 이용하여 고쳐보세요!

'Help! Help! I\'m being repressed!'



# 22

"""
문자열 "PYTHON"은 여섯개의 문자를 가지고 있고,
아래와 같이 0부터 5까지 숫자가 매겨져 있습니다:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

따라서 여러분이 "Y"를 원한다면, 다음과 같이 작성하면 됩니다:
"PYTHON"[1] (언제나 순서는 0부터 세기 시작합니다!)
"""
fifth_letter = "MONTY"[4]

print fifth_letter



# 23

parrot = "Norwegian Blue"
print len(parrot)



# 24

parrot = "Norwegian Blue"

print parrot.lower()



# 25

parrot = "norwegian blue"

print parrot.upper()



# 26

"""네 번째 줄에서 변수를 선언하고 값을 지정하세요.
그런 다음 다섯 번째 줄에서 메소드를 호출하세요!"""

pi = 3.14
print str(pi)



# 27

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()



# 28

"""네 번째 줄에서 파이썬에게 "Monty Python"을
console에 출력하라고 전하세요!"""

print "Monty Python"



# 29

"""다섯 번째 줄에 변수 the_machine_goes
를 선언하고 문자열 "Ping!"을 값으로 지정하세요.
그런 다음, 여섯 번째 줄에서 변수를 출력하세요!"""

the_machine_goes = "Ping!"
print the_machine_goes



# 30

# 세 번째 줄에서 "Spam and eggs"의 연결된 문자열을 출력하세요!

print "Spam " + "and " + "eggs"



# 31

# 세 번째 줄에서 숫자 3.14를 문자열로 바꿔보세요!

print "The value of pi is around " + str(3.14)



# 32

string_1 = "카멜롯"
string_2 = "장소"

print "%s 으로 돌아가지 말자. 그곳은 멍청한 %s 이다." % (string_1, string_2)



# 33

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)



# 34

# 아래의 세 번째 줄부터 코드를 작성하세요!

my_string = "hello world"
print len(my_string)
print my_string.upper()



# 35

from datetime import datetime



# 36

from datetime import datetime

now = datetime.now()

print now



# 37

from datetime import datetime

now = datetime.now()

print now

current_year = now.year
current_month = now.month
current_day = now.day

print current_year
print current_month
print current_day



# 38

from datetime import datetime

now = datetime.now()

c_y = now.year
c_m = now.month
c_d = now.day

print str(c_m) + "/" + str(c_d) + "/" + str(c_y)



# 39

from datetime import datetime

now = datetime.now()

c_y = now.year
c_m = now.month
c_d = now.day
c_h = now.hour
c_m2 = now.minute
c_s = now.second

print str(c_m) + "/" + str(c_d) + "/" + str(c_y) + str(c_h) + ":" + str(c_m2) + ":" + str(c_s)



# 40

from datetime import datetime

now = datetime.now()

c_y = now.year
c_m = now.month
c_d = now.day
c_h = now.hour
c_m2 = now.minute
c_s = now.second

print str(c_m) + "/" + str(c_d) + "/" + str(c_y) + " " + str(c_h) + ":" + str(c_m2) + ":" + str(c_s)



# 41

def clinic():
    print "여러분은 방금 막 치과에 들어섰습니다!"
    print "왼쪽 문과 오른쪽 문, 둘 중에 어떤 문으로 들어가시겠습까?"
    answer = raw_input("왼쪽이면 left, 오른쪽이면 right 라고 입력하고 'Enter'를 누르세요.").lower()
    if answer == "left" or answer == "l":
        print "이런, 방을 잘못 들어왔습니다!"
    elif answer == "right" or answer == "r":
        print "사랑니를 뽑기로 했군요, 행운을 빕니다!"
    else:
        print "왼쪽이나 오른쪽, 둘 중 아무것도 선택하지 않았군요! 다시 해보세요."
        clinic()

clinic()



# 42 ★

# 아래의 각 변수들에 적합한 True 또는 False 값을 할당하세요!
bool_one = 17 < 118 % 100

bool_two = 100 == 33 * 3 + 1

bool_three = 19 <= 2 ** 4

bool_four = -22 >= -18

bool_five = 99 != 98 + 1

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five



# 43 ★

# 아래의 각 변수들에 적합한 True 또는 False 값을 할당하세요!

bool_one = 20 + -10 * 2 > 10 % 3 % 2

bool_two = (10 + 17) ** 2 == 3 ** 6

bool_three = 1 ** 2 ** 3 <= -(-(-1))

bool_four = 40 / 20 * 4 >= -4 ** 2

bool_five = 100 ** 0.5 != 6 + 4

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five



# 44

# 아래의 각 변수들이 알맞은 불린값을 갖도록 비교문을 작성하세요!

# 변수의 값이 참이 되도록 만드세요!
bool_one = 1 == 1

# 변수의 값이 거짓이 되도록 만드세요!
bool_two = 1 != 1

# 변수의 값이 참이 되도록 만드세요!
bool_three = 2 >= 1

# 변수의 값이 거짓이 되도록 만드세요!
bool_four = 3 <= 1

# 변수의 값이 참이 되도록 만드세요!
bool_five = 5 < 9

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five



# 45

"""
     불린 연산자(Boolean Operators)
-----------------------------------------------
True 그리고(and) True의 결과는 True
True 그리고(and) False의 결과는 False
False 그리고(and) True의 결과는 False
False 그리고(and) False의 결과는 False

True 또는(or) True의 결과는 True
True 또는(or) False의 결과는 True
False 또는(or) True의 결과는 True
False 또는(or) False의 결과는 False

True 부정(not)의 결과는 False
False 부정(not)의 결과는 True

"""



# 46 ★

bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five



# 47

bool_one = True
# 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True
# True or False

bool_three = False
# 100**0.5 >= 50 or False

bool_four = True
# True or True

bool_five = False
# 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1



# 48

bool_one = False
# not True

bool_two = True
# not 3**4 < 4**3

bool_three = True
# not 10 % 3 <= 10 % 2

bool_four = True
# not 3**2 + 4**2 != 5**2

bool_five = False
# not not False



# 49

bool_one = False
# False or not True and True

bool_two = True
# False and not True or True

bool_three = True
# True and no (False or False)

bool_four = True
# not not True or False and not True

bool_five = False
# False or not (True and True)



# 50

# 아래의 각 변수들이 알맞은 불린값을 갖도록 수식을 작성하세요!

# 변수의 값이 거짓이 되도록 만드세요!
bool_one = not True

# 변수의 값이 참이 되도록 만드세요!
bool_two = True and True

# 변수의 값이 거짓이 되도록 만드세요!
bool_three = True and False

# 변수의 값이 참이 되도록 만드세요!
bool_four = True or False

# 변수의 값이 참이 되도록 만드세요!
bool_five = not False and not False



# 51

