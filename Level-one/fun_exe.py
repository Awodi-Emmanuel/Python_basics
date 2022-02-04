###################
#### Problem 1 ####
###################
# Given a list of integers, return True if the sequence of numbers 1,2,3
# appears in the list somewhere.

def array_check(nums):  
    for i in range(len(nums)-2):
        if nums[1]==1 and nums[i+1]==2 and nums[i+2]==3:
          return True
    return False    
print(array_check([1,1,2,3,1]))
print(array_check([1,1,2,4,1]))
print(array_check([1,1,2,1,2,3]))  
#########################
#### -- PROBLEM 2 -- ####
#########################
def string_bits(str):
    return str[::2]
print(string_bits('Hello'))  
print(string_bits('Hi'))    
print(string_bits('Heeololeo')) 

# His solution for problem 2
def str_bits(mystrg):
    result = ""
    for i in range(len(mystrg)):
        if i%2 ==0:
            result = result +mystrg[i]
    return result      
print(str_bits('Hello'))  
print(str_bits('Hi'))    
print(str_bits('Heeololeo'))   

#########################
#### -- PROBLEM 3 -- ####
#########################
def end_other(a,b):
    if a[-1].lower() == b[-1].lower():
        return True   
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

# CORRECTION FOR THE PROBLEM 3
def end_oder(h,k):
   h = h.lower()
   k = k.lower()
#    return (k.endswith(a) or h.endswith(b))
   return h[-(len(k)):]==k or h == k[-len(h):]
print(end_oder('Hiabc', 'abc'))
print(end_oder('AbC', 'HiaBc'))
print(end_oder('abc', 'abXabc'))    
#########################
#### -- PROBLEM 4 -- ####
#########################
def double_char(str2):
    result = ""
    for char in str2:
        result += char*2
        return result

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
  

#########################
#### -- PROBLEM 5 -- ####
#########################

# """
# def no_teen_sum(a,b,c):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)

# def fix_teen(n):
#     if n [13,14,17,18,19]:
#         return 0
#     return n
# print(no_teen_sum(1,2,3))    
# print(no_teen_sum(2,13,1))    
# print(no_teen_sum(2,1,14))
# """

#########################
#### -- PROBLEM 6 -- ####
#########################

def count_evens(nums):
    count = 0
    for element in nums:
        if element %2 == 0:
            count +=1
    return count

print(count_evens([2,1,2,3,4]))
print(count_evens([2,1,2,3,4]))
print(count_evens([2,1,2,3,4]))