1
def string_times(str, n):
    return str*n
    
print(string_times('Hi', 3))
print(string_times('x', 4))
print(string_times('code', 3))


2
def front_times(str,n):
    return str[:3]*n if len(str)>=3 else str*n
    
print(front_times('Chocolate', 3))
print(front_times('Ab', 4))
print(front_times('Abc', 0))


3
def string_bits(str):
    newStr = ""
    for i in str[:len(str):2]:
        newStr += i
    return newStr
    
print(string_bits('Hello'))


4
def string_splosion(str):
    newStr = ''
    for i in range(len(str)+1):
        newStr += str[:i]
    return newStr

print(string_splosion('Code'))
print(string_splosion('Kitten'))


5
def last2(str):
    count = 0
    for i in range(len(str)-2):
        if str[i:i+2] == str[-2:]:
            count +=1
    return count
    
print(last2('axxxaaxx'))


6
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9, 3, 9]))
print(array_count9([4, 2, 4, 3, 1]))


7
def array_front9(nums):
    return 9 in nums[:4]

print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 9]))


8
def array123(nums):
    for i in range(len(nums[:-2])):
        if nums[i:i+3] == [1,2,3]:
            return True
        else:
            continue
    return False

print(array123([1, 1, 2, 1, 2, 3]))
print(array123([1, 1, 2, 4, 1]))


9
def string_match(a,b):
    count = 0
    for i in range(len(a)-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))