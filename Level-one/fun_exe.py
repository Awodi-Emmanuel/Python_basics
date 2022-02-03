###################
#### Problem 1 ####
###################
# Given a list of integers, return True if the sequence of numbers 1,2,3
# appears in the list somewhere.

# For example:

# arrayCheck([1,1,2,3,1]) -> True
# arrayCheck([1,1,2,4,1]) -> False
# arrayCheck([1,1,2,1,2,3]) -> True


def array_check(nums): 
    for i in range(len(nums)-2):
        if nums[1]==1 and nums[i+1]==2 and nums[i+2]==3:
          return True
    return False    
print(array_check([1,1,2,3,1]))
print(array_check([1,1,2,4,1]))
print(array_check([1,1,2,1,2,3]))  

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


def end_other(a,b):
    if a[-1].lower() == b[-1].lower():
        return True   
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

# CORRECTION FOR THE CODE ABOVE
def end_oder(h,k):
   h = h.lower()
   k = k.lower()
#    return (k.endswith(a) or h.endswith(b))
   return h[-(len(k)):]==k or h == k[-len(h):]
print(end_oder('Hiabc', 'abc'))
print(end_oder('AbC', 'HiaBc'))
print(end_oder('abc', 'abXabc'))    

def double_char(str2):
    return str2 * 2

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
  

#########################
#### -- PROBLEM 5 -- ####
#########################


def no_teen_sum(a,b,c):
    return a + b + c
print(no_teen_sum(1,2,3))    
print(no_teen_sum(2,13,1))    
print(no_teen_sum(2,1,14))

# def count_evens(nums):
#     for in

# print(even(count_even([2,1,2,3,4])))
# print(count_even([2,1,2,3,4]))
# print(count_even([2,1,2,3,4]))