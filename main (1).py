
# Online Python - IDE, Editor, Compiler, Interpreter

# define the functions
def add(a, b):
    return a + b
 
def subrtact(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b

# select operations

print("Select operations:")
print("1: Add")
print("2: Subtract")
print("3:Multiply")
print("4:Divide")

while True:
    choice  = input("Ënter choice 1/2/3/4")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ënter First number: "))
            num2 = float(input("Ënter Second number: "))
        except ValueError:
            print("Ïnvalid Input. Please Enter Enter a Number.")
            
        if choice == '1':
            print(num1, "+", num2, "=" , add(num1, num2))
            
        elif choice =='2':
            print(num1, "-", num2, "=" , subtract(num1, num2))
            
        elif choice =='3':
            print( num1, "*", num2, "=" , multiply(num1, num2))
            
        elif choice == '4':
            print(num1, "/", num2, "=" , divide(num1, num2))
        
        next_calculation = input("Do the next calculation, (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")
 
        # TODO: write code...
    
