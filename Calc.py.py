# Calculator Program in Python
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y
def subtraction(x,y):
    return x-y
def addition(x,y):
    return x+y
def square(x,y):
    return x*x
def remainder(x,y):
    return x%y


print("Select operation:")
print("1. DIVISION")
print("2. MULTIPLICATION")
print("3. SUBTRACTION")
print("4. ADDITION")
print("5. SQUARE")
print("6. REMAINDER")

while True:
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4','5','6'):
        try:
            num1 = int(input("Enter 1st number: "))
            num2 = int(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == '1':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '2':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '3':
            print(num1, "-", num2, "=", subtraction(num1, num2))
        elif choice == '4':
            print(num1, "+", num2, "=", addition(num1, num2))
        elif choice == '5':
            print(num1, "*", num1, "=", square(num1,num2))
        elif choice =='6':
            print(num1, "%", num2, "=", remainder(num1,num2))

        next_calculation = input("Continue?(y/n) : ")
        if next_calculation.lower() == "n":
            break
    else:
        print("Invalid Choice")
    
