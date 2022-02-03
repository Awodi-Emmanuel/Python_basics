my_list = [1,2,3,4,5,6,7,8]
def my_func(num):
    return num%2 == 0
evens = filter(my_func,my_list)
print(list(evens))

# LAMBDA EXPRESSION
# lambda expression is break down of any function in python 
even_no = filter(lambda num_input:num_input%2 == 0, my_list)
print(list(even_no))    