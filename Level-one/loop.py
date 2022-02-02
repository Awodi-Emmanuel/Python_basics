# For Loop

seq = [1,2,3,4,5,6,7]

for x in seq:
    print(x)
    
#   Looping through Dictionary words 
my_dict = {"John":1, "Dan":2, "mark":3}  

for v in my_dict:
    print([v])
    print(my_dict[v])
    
    
my_tuples = [(1,2), (3,4), (5,6)]
# To unpack the tuple in my for loop 
for tup1,tup2 in my_tuples:
    print(tup1)
    print(tup2)
        
        
#FOR LOOP

for item in range(10):
    print(item)
        
x = [1,2,3,4,5,6] 
out = []
for num in x: 
    out.append(num**2)
print(out)    

#list comprehension 

y = [1,2,3,4,5,6]

loop_through = [nums**3 for nums in y]
print(loop_through)
