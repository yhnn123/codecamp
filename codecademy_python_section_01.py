# 1

print "Welcom to Python!"
print "hi"



# 2

my_variable = 10

print my_variable



# 3

# �ռ� ���� ������ ����� ������ �� ������ ������ �����ϼ���!

my_int = 7
my_float = 1.23
my_bool = True

print my_int
print my_float
print my_bool



# 4

# �Ʒ��� ���� my_int�� ���� 7�� �����Ǿ� �ֽ��ϴ�.
# ������ ���� 3���� �����ϰ� ����� ����Ϸ��� ��� �ؾ��ұ��?

my_int = 7

# ���� ��° �ٿ��� ���� my_int�� ���� 3 ���� �����ϼ���!

my_int = 3

# ���� my_int�� ���� console�� ����ϴ� �ڵ�� �Ʒ��� �����ϴ�:
# ���⼭ ���� print Ű����� ���� �� �ڼ��� �ٷ� �����Դϴ�!

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

mysterious_variable = 42 # �ּ��̴�



# 9

""" �ּ��̴�
�ּ��̴�
�ּ��̴�
��
��
��
�� """



# 10

# �� ��° �ٿ��� ���� count_to�� ������ 1 ���ϱ� 2�� �����ϼ���!

count_to = 1+2

print count_to



# 11

# �� ��° �ٿ��� �ŵ������� �̿��Ͽ� ���� eggs�� ���� 100���� �����ϼ���!

eggs = 10 ** 2

print eggs



# 12

# �� ��° �ٿ��� ���� ������ �̿��Ͽ� ���� spam�� ���� 1�� �����ϼ���!

spam = 5 % 2

print spam



# 13

# �ּ��� �ۼ��Ϸ� ����

monty = True
python = 1.234
monty_python = python ** 2

print monty
print python
print monty_python



# 14

# �� ��° �ٿ� ���� variable�� ������ 44.50�� �����ϼ���!

meal = 44.50 



# 15

meal = 44.50

tax = 0.0675



# 16

# ���� �� �ƽ��ϴ�! �ټ� ��° �ٿ� ���� tip�� �����ϼ���.

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

# ���� ��° �ٿ� ���� total�� �����ϼ���!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)



# 19

# �� ��° �ٿ� ���� brain�� �����ϼ���!

brian = "������ ���� �������� ���� ���Ǽ���!"



# 20

# �� �ٸ��� �ϳ���, �������� �����ϰ� ���� �����ϼ���!

caesar = "Graham"
praline = "John"
viking = "Teresa"

# �������� �� �� ���� �ۼ��Ǿ�� �մϴ�.

print caesar
print praline
print viking


# 21

# �Ʒ��� ���ڿ��� ������ �ֽ��ϴ�. �齽������ �̿��Ͽ� ���ĺ�����!

'Help! Help! I\'m being repressed!'



# 22

"""
���ڿ� "PYTHON"�� �������� ���ڸ� ������ �ְ�,
�Ʒ��� ���� 0���� 5���� ���ڰ� �Ű��� �ֽ��ϴ�:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

���� �������� "Y"�� ���Ѵٸ�, ������ ���� �ۼ��ϸ� �˴ϴ�:
"PYTHON"[1] (������ ������ 0���� ���� �����մϴ�!)
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

"""�� ��° �ٿ��� ������ �����ϰ� ���� �����ϼ���.
�׷� ���� �ټ� ��° �ٿ��� �޼ҵ带 ȣ���ϼ���!"""

pi = 3.14
print str(pi)



# 27

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()



# 28

"""�� ��° �ٿ��� ���̽㿡�� "Monty Python"��
console�� ����϶�� ���ϼ���!"""

print "Monty Python"



# 29

"""�ټ� ��° �ٿ� ���� the_machine_goes
�� �����ϰ� ���ڿ� "Ping!"�� ������ �����ϼ���.
�׷� ����, ���� ��° �ٿ��� ������ ����ϼ���!"""

the_machine_goes = "Ping!"
print the_machine_goes



# 30

# �� ��° �ٿ��� "Spam and eggs"�� ����� ���ڿ��� ����ϼ���!

print "Spam " + "and " + "eggs"



# 31

# �� ��° �ٿ��� ���� 3.14�� ���ڿ��� �ٲ㺸����!

print "The value of pi is around " + str(3.14)



# 32

string_1 = "ī���"
string_2 = "���"

print "%s ���� ���ư��� ����. �װ��� ��û�� %s �̴�." % (string_1, string_2)



# 33

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)



# 34

# �Ʒ��� �� ��° �ٺ��� �ڵ带 �ۼ��ϼ���!

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
    print "�������� ��� �� ġ���� �����ϴ�!"
    print "���� ���� ������ ��, �� �߿� � ������ ���ðڽ���?"
    answer = raw_input("�����̸� left, �������̸� right ��� �Է��ϰ� 'Enter'�� ��������.").lower()
    if answer == "left" or answer == "l":
        print "�̷�, ���� �߸� ���Խ��ϴ�!"
    elif answer == "right" or answer == "r":
        print "����ϸ� �̱�� �߱���, ����� ���ϴ�!"
    else:
        print "�����̳� ������, �� �� �ƹ��͵� �������� �ʾұ���! �ٽ� �غ�����."
        clinic()

clinic()



# 42 ��

# �Ʒ��� �� �����鿡 ������ True �Ǵ� False ���� �Ҵ��ϼ���!
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



# 43 ��

# �Ʒ��� �� �����鿡 ������ True �Ǵ� False ���� �Ҵ��ϼ���!

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

# �Ʒ��� �� �������� �˸��� �Ҹ����� ������ �񱳹��� �ۼ��ϼ���!

# ������ ���� ���� �ǵ��� ���弼��!
bool_one = 1 == 1

# ������ ���� ������ �ǵ��� ���弼��!
bool_two = 1 != 1

# ������ ���� ���� �ǵ��� ���弼��!
bool_three = 2 >= 1

# ������ ���� ������ �ǵ��� ���弼��!
bool_four = 3 <= 1

# ������ ���� ���� �ǵ��� ���弼��!
bool_five = 5 < 9

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five



# 45

"""
     �Ҹ� ������(Boolean Operators)
-----------------------------------------------
True �׸���(and) True�� ����� True
True �׸���(and) False�� ����� False
False �׸���(and) True�� ����� False
False �׸���(and) False�� ����� False

True �Ǵ�(or) True�� ����� True
True �Ǵ�(or) False�� ����� True
False �Ǵ�(or) True�� ����� True
False �Ǵ�(or) False�� ����� False

True ����(not)�� ����� False
False ����(not)�� ����� True

"""



# 46 ��

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

# �Ʒ��� �� �������� �˸��� �Ҹ����� ������ ������ �ۼ��ϼ���!

# ������ ���� ������ �ǵ��� ���弼��!
bool_one = not True

# ������ ���� ���� �ǵ��� ���弼��!
bool_two = True and True

# ������ ���� ������ �ǵ��� ���弼��!
bool_three = True and False

# ������ ���� ���� �ǵ��� ���弼��!
bool_four = True or False

# ������ ���� ���� �ǵ��� ���弼��!
bool_five = not False and not False



# 51

