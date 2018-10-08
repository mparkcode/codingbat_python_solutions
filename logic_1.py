# 1
# def cigar_party(cigars, is_weekend):
#     return cigars >= 40 if is_weekend else cigars>= 40 and cigars <=60
    
# print(cigar_party(30, False))
# print(cigar_party(50, False))
# print(cigar_party(70, True))


# 2
# def date_fashion(you, date):
#     if (you <= 2) or (date <= 2):
#         return 0
#     elif(you >= 8) or (date >=8):
#         return 2
#     else:
#         return 1

# print(date_fashion(5, 10))
# print(date_fashion(5, 2))
# print(date_fashion(5, 5))


# 3
# def squirrel_play(temp, is_summer):
#     return temp>=60 and temp<=100 if is_summer else temp>=60 and temp<=90
    
# print(squirrel_play(70, False))
# print(squirrel_play(95, False))
# print(squirrel_play(95, True))


# 4
# def caught_speeding(speed, is_birthday):
#     if is_birthday:
#         if speed <=65:
#             return 0
#         elif speed <= 85:
#             return 1
#         else:
#             return 1
#     else:
#         if speed <=60:
#             return 0
#         elif speed <= 80:
#             return 1
#         else:
#             return 1
            
# print(caught_speeding(60, False))
# print(caught_speeding(65, False))
# print(caught_speeding(65, True))


# 5
# def sorta_sum(a,b):
#     return 20 if a+b>=10 and a+b<=19 else a+b
    
# print(sorta_sum(3, 4))
# print(sorta_sum(9, 4))
# print(sorta_sum(10, 11))


# 6
# def alarm_clock(day,vacation):
#     if vacation:
#         if day == 0 or day == 6:
#             return "off"
#         else:
#             return "10:00"
#     else:
#         if day == 0 or day == 6:
#             return "10:00"
#         else:
#             return "7:00"
            
# print(alarm_clock(1, False))
# print(alarm_clock(5, False))
# print(alarm_clock(0, False))
# print(alarm_clock(0, True))


# 7
# def love6(a,b):
#     return a==6 or b==6 or a+b==6 or a-b==6 or b-a==6
    
# print(love6(6, 4))
# print(love6(4, 5))
# print(love6(1, 5))


# 8
# def in1to10(n, outside_mode):
#     return n<=1 or n>=10 if outside_mode else n>=1 and n<=10

# print(in1to10(5, False))
# print(in1to10(11, False))
# print(in1to10(11, True))


9
def near_ten(num):
    return num%10 <=2 or num%10 == 8 or num%10 == 9
    
print(near_ten(12))
print(near_ten(17))
print(near_ten(19))