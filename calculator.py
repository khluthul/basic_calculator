def get_number():
    num = input("Enter a number:\n")
    while True:
        if num.isdigit():
            return num
        else:
            num  = input("Plese enter a number:\n")


def get_operator():
    operators = ['/' ,'-', '*', '+']
    op = input("Enter an operand:\n")
    while True:
        if op in operators:
            return op
        else:
            op = input("Invalid operand.\nEnter an operand:\n")


def work_out_sum(one, two, op):
    if op == '+':
        print(f'{int(one) + int(two)}')
    elif op == '-':
        print(f'{int(one) - int(two)}')
    elif op == '*':
        print(f'{int(one) * int(two)}')
    elif op == '/':
        print(f'{int(one) / int(two)}')
    


one = get_number()
op = get_operator()
two = get_number()
work_out_sum(one, two, op)