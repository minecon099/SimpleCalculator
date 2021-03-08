print("Welcome to a Python Based Calculator")
print("Use this Chart to Pick an operation")
print("Sum = 1")
print("Substract = 2")
print("Multiply = 3")
print("Divide = 4")

number_one = int(input("Type 1'st Number:"))
number_two = int(input("Type 2'nd Number:"))
operation_number = int(input("Type Operation Number or 0 to End:"))

while operation_number != 0:
    if operation_number == 1:
        result1 = number_one + number_two
        result2 = number_two + number_one
        print("The results are:",result1, result2)
        operation_number = int(input("Type Operation Number or 0 to End:"))
    elif operation_number == 2:
       result1 = number_one - number_two
       result2 = number_two - number_one
       print("The results are:",result1, result2) 
       operation_number = int(input("Type Operation Number or 0 to End:"))
    elif operation_number == 3:
       result1 = number_one * number_two
       result2 = number_two * number_two
       print("The results are:",result1, result2)
       operation_number = int(input("Type Operation Number or 0 to End:"))
    elif operation_number == 4:
       result1 = number_one / number_two
       result2 = number_two / number_one
       print("The results are:",result1, result2)
       operation_number = int(input("Type Operation Number or 0 to End:"))
    else:
        print("Invalid Operator!")
        operation_number = int(input("Type Operation Number or 0 to End:"))
        
print("Thanks for using this calculator, stay tuned for more updates")        
print("Discord: Pogamepayer#3492 / GitHub: minecon099")        
