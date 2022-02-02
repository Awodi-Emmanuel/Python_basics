# Return call back if integer is correct

def add_num(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers!"
result = add_num(2,3)
print(result)    