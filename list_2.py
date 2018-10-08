1
def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count
    
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))


2
def big_diff(nums):
    return max(nums) - min(nums)
    
print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))


3
def centered_average(nums):
    nums.sort()
    return int(sum([i for i in nums[1:-1]])/len([i for i in nums[1:-1]]))
    
print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))


4
def sum13(nums):
    nums.append(0)
    nl = []
    for i in range(0, len(nums)-1,2):
        if nums[i] == 13:
            continue
        if nums[i-1] != 13:
            nl.append(nums[i])
        if nums[i+1] and nums[i+1] != 13:
            nl.append(nums[i+1])
    return sum(nl)

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))


5
def sum67(nums):
    add = True
    count = 0
    for i in range(len(nums)):
        if nums[i] == 6:
            add = False
        if nums[i-1] == 7 and nums[i] != 6:
            add = True
        if add == True:
            count += nums[i]
    return count
    
print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))


6
def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2:
            if nums[i+1] == 2:
                return True
            continue
    return False
    
print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))