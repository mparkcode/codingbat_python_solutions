# 1
# def make_bricks(small,big,goal):
#     return goal%5<=small if big*5>goal else big*5+small>=goal
    
# print(make_bricks(3, 1, 8))
# print(make_bricks(3, 1, 9))
# print(make_bricks(3, 2, 10))


# 2
# def lone_sum(a,b,c):
#     sum = 0
#     if a!=b and a!=c:
#         sum+=a
#     if b!=a and b!=c:
#         sum+=b
#     if c!=a and c!=a:
#         sum+=c
#     return sum
    
# print(lone_sum(1, 2, 3))
# print(lone_sum(3,2,3))
# print(lone_sum(3,3,3))
    

# 3
# def lucky_sum(a,b,c):
#     if a == 13:
#         return 0
#     elif b == 13:
#         return a
#     elif c == 13:
#         return a+b
#     else:
#         return a+b+c
        
# print(lucky_sum(1, 2, 3))
# print(lucky_sum(1, 2, 13))
# print(lucky_sum(1, 13, 3))
# print(lucky_sum(13, 1, 3))


# 4
# def fix_teen(n):
#     return n if n==15 or n==16 or n<13 or n>19 else 0
    
# def no_teen_sum(a,b,c):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)
    
# print(no_teen_sum(1, 2, 3))
# print(no_teen_sum(2, 13, 1))
# print(no_teen_sum(2, 1, 14))
# print(no_teen_sum(2, 1, 15))


# 5
# def round10(num):
#     return num + 10 - num%10 if num%10>=5 else num - num%10
    
# def round_sum(a,b,c):
#     return round10(a) + round10(b) + round10(c)
    
# print(round_sum(16, 17, 18))
# print(round_sum(12, 13, 14))
# print(round_sum(6, 4, 4))

# 6
# def close_far(a,b,c):
#     if abs(a-b) <= 1:
#         return abs(a-c)>=2 and abs(b-c)>=2
#     if abs(a-c) <= 1:
#         return abs(b-c)>=2 and abs(b-a)>=2
#     else:
#         return abs(a-c)>=2 and abs(b-a)>=2
        
# print(close_far(1, 2, 10))
# print(close_far(1, 2, 3))
# print(close_far(4, 1, 3))


# 7
# def make_chocolate(small,big,goal):
#     if big*5 >= goal:
#         return goal%5 if goal%5 <=small else -1
#     elif big*5 + small >= goal:
#         return goal - big*5
#     else:
#         return -1
        
        
# print(make_chocolate(4, 1, 9))
# print(make_chocolate(4, 1, 10))
# print(make_chocolate(4, 1, 7))