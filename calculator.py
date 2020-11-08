# digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# dec = '.'
operators = ['+', '-', '*', '/']

def get_sum():
    ''' THIS FUNCTION TAKES IN DIGITS AND OPERATORS FROM USER'''
    digits = input('Enter a number: ')
    list_ = list(digits)
    fl = 0
    while True:
        num = []
        if digits == '':
            digits = input('Please enter a number: ')
        else:
            for i in digits:
                if i.isdigit() or i == '.':
                    num.append(i)
                    print('####################\n')
                    print(num)
                else:
                    # num = []
                    # print(num)
                    digits = get_sum()
            return ""join.num
        # break


num = get_sum()
# print(num)