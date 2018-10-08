1
def double_char(str):
    newStr = ""
    for i in range(len(str)):
        newStr += str[i]*2
    return newStr
    
print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))


2
def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i]+str[i+1] == 'hi':
            count += 1
    return count
    
print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))


3
def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str)-2):
        if str[i]+str[i+1]+str[i+2] == 'cat':
            cat_count += 1
        if str[i]+str[i+1]+str[i+2] == 'dog':
            dog_count += 1
    return cat_count == dog_count
    
print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))


4
def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i]+str[i+1] == 'co' and str[i+3]=='e':
            count += 1
    return count
    
print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('AAcodeBBcoleCCccoreDD'))


5
def end_other(a,b):
    return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())
    
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))


6
def xyz_there(str):
    if len(str)>=3:
        for i in range(len(str)-2):
            if str[i]+str[i+1]+str[i+2] == 'xyz':
                if str[i-1] == '.':
                    continue
                return True
    return False
    
print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))