1
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6
    
print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))


2
def same_first_last(nums):
    return len(nums)>=1 and nums[0] == nums[-1]
    
print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))


3
def make_pi():
    return[3,1,4]


4
def common_end(a,b):
    return a[0] == b[0] or a[-1] == b[-1]
    
print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))


5
def sum3(nums):
    return sum(nums)
    
print(sum3([1, 2, 3]))
print(sum3([5, 11, 2]))
print(sum3([7, 0, 0]))


6
def rotate_left3(nums):
    newNums = [nums[1],nums[2],nums[0]]
    return newNums

print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))


7
def reverse3(nums):
    new_nums = [nums[2], nums[1], nums[0]]
    return new_nums
    
print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))


8
def max_end3(nums):
    big = max(nums[0], nums[-1])
    for i in range(len(nums)):
        nums[i] = big
    return nums

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))


9
def sum2(nums):
    return sum(nums[:2]) if len(nums)>2 else sum(nums)
    
print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))


10
def middle_way(a,b):
    return [a[1],b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))


11
def make_ends(nums):
    return [nums[0], nums[-1]]
    
print(make_ends([1, 2, 3]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))


12
def has23(nums):
    return 2 in nums or 3 in nums
    
print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))