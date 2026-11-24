def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def power(a,b):
    return a** b

def devide(a,b):
    if b==0:
        return None
    return a/b

def show_menue():
    print('==== Claculator ==== \n')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Devide')
    print('5. Power')
    print('0. Exit')

def Main():
    count = 0
    while True:
        show_menue()
        choice = input('Choice: ')
        
        if choice =='0':
            print(f"total calclation: {count}")
            break
        
        if choice not in ('1','2','3','4','5'):
            print("Invalid option,try again")
            continue
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if choice == "1":
            result = add(num1,num2)
        elif  choice == "2":
            result = sub(num1,num2)
        elif  choice == "3":
            result = multiply(num1,num2)
        elif  choice == "4":
            result = devide(num1,num2)
        elif  choice == "5":
            result = power(num1,num2)
        
        if result is None:
            print('error: cannot devide by 0')
        else:
            print(f"Result: {result}")
            count =+1
if __name__=="__main__":
    Main()