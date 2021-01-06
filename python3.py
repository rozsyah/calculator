print("Calculator Terminal")
while True:
    print('Options:')
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_info = input(': ')

    if user_info == "quit":
        print('exit. please following page instagram @r0zsyah')
        break
    elif user_info == "add":
        num1 = float(input('Enter your first num: '))
        num2 = float(input('Enter your secound num: '))
        tabdel = str(num1 + num2)
        print('G: '+ tabdel)
    elif user_info == "subtract":
        num1 = float(input('Enter your first num: '))
        num2 = float(input('Enter your secound num: '))
        tabdel = str(num1 - num2)
        print('G: '+ tabdel)
    elif user_info == "multipy":
        num1 = float(input('Enter your first num: '))
        num2 = float(input('Enter your secound num: '))
        tabdel = str(num1 * num2)
        print('G: '+ tabdel)
    elif user_info == "divide":
        num1 = float(input('Enter your first num: '))
        num2 = float(input('Enter your secound num: '))
        tabdel = str(num1 / num2)
        print('G: '+ tabdel)
