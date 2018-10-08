1 
def sleep_in(weekday, vacation):
    return not(weekday) or vacation
    
print(sleep_in(False, True))


2
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

print(monkey_trouble(False, False))


3
def sum_double(a,b):
    return (a+b)*2 if a==b else a+b
    
print(sum_double(3,3))
print(sum_double(2,3))


4
def diff21(n):
    return (n-21)*2 if n>21 else 21-n
    
print(diff21(30))
print(diff21(19))


5
def parrot_trouble(talking,hour):
    return talking and (hour<7 or hour>20)
    
print(parrot_trouble(True, 6))
print(parrot_trouble(True, 21))
print(parrot_trouble(True, 10))
print(parrot_trouble(False, 3))


6
def makes10(a,b):
    return a==10 or b==10 or a+b==10
    
print(makes10(10,2))
print(makes10(2,10))
print(makes10(2,8))
print(makes10(3,8))


7 
def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200-n) <= 10
    
print(near_hundred(99))
print(near_hundred(104))
print(near_hundred(67))
print(near_hundred(112))
print(near_hundred(199))
print(near_hundred(204))
print(near_hundred(167))
print(near_hundred(212))


8
def pos_neg(a, b, negative):
    return a<0 and b <0 if negative else (a<0 and b>0) or (a>0 and b<0)
    
print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
print(pos_neg(-4, -5, False))


9
def not_string(str):
    return str if str[:3]=='not' else 'not '+str
    
print(not_string('mike'))
print(not_string('not mike'))


10
def missing_char(str,n):
    return str[:n]+str[n+1:]

print(missing_char('kitten', 1))
print(missing_char('Hi', 0))
print(missing_char('code', 1))
print(missing_char('chocolate', 8))


11
def front_back(str):
    return str[-1:] + str[1:-1] + str[:1] if len(str)>1 else str

print(front_back('code'))
print(front_back('Chocolat'))
print(front_back("a"))
print(front_back(""))


12
def front3(str):
    return str[:3]*3 if len(str)>3 else str*3
    
print(front3('Java'))
print(front3('abc'))
print(front3('ab'))
print(front3(''))