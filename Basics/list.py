from audioop import reverse


my_list = [1, 2, 3, 4]
print(my_list)
mylist = ['Django', 'Nodejs', 'Laravel']
print(len(mylist))

# LIST REASSIGNMENT

list_assign = ['a', 'b', 'c', 'd', 'e']
print('before reasignment:')

list_assign[0] = 'New Item:'
print("After reasignments")

print((list_assign))

# NEST LIST

mylist = [1, 2, 3,['a', 'b', 'c']]

print(mylist[1])

# LIST COMPREHENSION  

matrix = [[1,2,3,], [4,5,6,],[7,8,9]]

first_col = [row[2] for row in matrix]

print(first_col)

