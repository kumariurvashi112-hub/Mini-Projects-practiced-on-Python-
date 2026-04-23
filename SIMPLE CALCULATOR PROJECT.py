def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    
    
    if y == 0:
        return "error!division by zero"
    else:
        return x//y
print("simple calculator")
print("1.Add") ### IT WILL PERFORM BY USING ADDITION  METHOD AND ALSO USE A + OPERATOR THEN PERFORM #
print("2.Subtract") ### IT WILL PERFORM BY USING SUBTRACT METHOD AND ALSO USE A - OPERATION FURTHER PERFORM ###
print("3.multiply") ### IT WILL PERFORM BY USING MULTIPLY METHOD AND ALSO USE A * OPERATION FURTHER PERFORM ###
print("4.divide") ### IT WILL PERFORM BY USING DIVISION  METHOD AND ALSO USE A // OPERATION FURTHER PERFORM ###

choice  = int(input("enter the choice between (1-4):")) ## TAKE INPUT FROM USER ###

num1 = int(input("enter the first number:"))## TAKE INPUT FROM USER ###
num2 = int(input("enter the second number:"))## TAKE INPUT FROM USER ##### TAKE INPUT FROM USER ###

if choice == 1:
    result = num1+num2
    print("the addition of num1 and num2 is:",result)
elif choice == 2:
    result = num1 - num2
    print("the subtraction of num1 and num2 is:",result)
elif choice == 3:
    result = num1 * num2
    print("the multiplication of num1 * num2 is:",result)
elif choice == 4:
    result = num1 // num2
    print("the division of num1 and num2 is :",result)
else:
    print("invalid operaton please choose a valid operation") ### FURTHE IF AND ELIF CHOICE ARE NOT EXECUTED THEN YOU CAN USE AND CALCULATE ELSE CONDITION STATEMENT ###
