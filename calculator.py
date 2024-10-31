def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations={"+":add,"-":substract,"*":multiply,"/":divide}
def calculate():
    def calculator_logo():
        logo = '''
         _____________________
        |  _________________  |
        | | PYTHON CALCULATOR | |
        | |_________________| |
        |  ___ ___ ___   ___  |
        | | 7 | 8 | 9 | | / | |
        | |___|___|___| |___| |
        | | 4 | 5 | 6 | | * | |
        | |___|___|___| |___| |
        | | 1 | 2 | 3 | | - | |
        | |___|___|___| |___| |
        | | . | 0 | = | | + | |
        | |___|___|___| |___| |
        |_____________________|

        '''
        print(logo)

    calculator_logo()

    num1=float(input("Enter the first number"))
    To_continue=True
    while To_continue:
            for symbols in operations:
                print(symbols)
            operation_symbol=input("Enter the symbol")
            num2=float(input("Enter the second number"))
            answer=operations[operation_symbol](num1,num2)
            print(f"The result of {num1}   {operation_symbol}  {num2} = {answer}")
            choice=input((f"Enter 'y' to continue with the result {answer} or press 'n' to start a new calculation"))
            if choice=='y':
                num1=answer

            else:
                print("\n"*20)
                To_continue=False
                calculate()
calculate()






