from audioop import  reverse
# my_list = [1,2, 3, 4, 5, 6, 7, 8]

# print(sum(my_list))




from ast import If
from re import X


def mult_items(items):
    num_muiltipler = 1
    for x in items:
        num_muiltipler *= x
    return num_muiltipler 



print(mult_items([1,2, 3, 4,]))



# def max_num(item):
#     maxNumber = list[0]
#     for x in item:
#         If x > maxNumber:
#             maxNumber = x:
#                 return maxNumber     
# print(my_list([1,2,3,4,5]))   
    
    
##############
## Problem 1##
##############  
    

# Given the string

s = 'django'

# Use in indexing to print out the folowing

# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan' 
print(s[0:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[4:6])


# Bonus: Use indexing to reverse the string 

print(s[::-1])



##############
## Problem 2 ##
##############  
 
# Given this nested list:   
l = [3,7,[1,4,'hello']]

#Reasign "hello" to th be "goodbye"
r = l[2]= 'goodbye'

print(r)


##############
## Problem 3 ##
##############  

# Using keys and indexing, grab the "hello" from the following dictionaries:

d1 = {'simple_key': 'hello'}

print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}

print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d3['k1'][0]['nest_key'][1][0])


##############
## Problem 4##
##############  

#Use a set to find a unique values of the list below:

mylist = [1, 1,1,1,1,2,2,2,2,3,3,3,3]

my_set = set(mylist)

print(my_set)



##############
## Problem 5 ##
##############  

# You are given two variables:

age = 4
name = "Sammy"

print(" Hello my dogs name is {a} and he is {b}year old".format(a=name,b=age))

