import re

def increment_space(space: int, value: str, char= ' ') -> str:
    str = ''

    for i in range(space-len(value)):
        str += char 

    str += value

    return str

def calculate(operator: str, num1: int, num2: int) -> int:
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2

def arithmetic_arranger(problems, show_answers=False):
    try:
        list_return = {
            'line1': '',
            'line2': '',
            'line3': '',
            'result': '',
        }

        str_return = ''

        if len(problems) > 5:
            raise Exception("Too many problems.")
        
        for prob in problems:
            info_prob = prob.split()

            operator = info_prob[1]
            num1 = info_prob[0]
            num2 = info_prob[2]

            if "+" != operator and "-" != operator:
                raise Exception("Operator must be '+' or '-'.")
            
            if not num1.isdigit() or not num2.isdigit():
                raise Exception("Numbers must only contain digits.")
            
            if len(num1) > 4 or len(num2) > 4:
                raise Exception("Numbers cannot be more than four digits.")

            result = calculate(operator, int(num1), int(num2))

            space = max(len(num1), len(num2))+2

            list_return['line1'] += f"{increment_space(space, num1)}    "
            list_return['line2'] += f"{operator}{increment_space(space-1, num2)}    "
            list_return['line3'] += f"{increment_space(space, '', '-')}    "
            list_return['result'] += f"{increment_space(space, str(result))}    "

        list_return['line1'] = list_return['line1'][:-4]+'\n'
        list_return['line2'] = list_return['line2'][:-4]+'\n'
        list_return['line3'] = list_return['line3'][:-4]+''
        list_return['result'] = list_return['result'][:-4]+''

        if show_answers:
            list_return['line3'] += '\n'
        else:
            list_return.pop('result')

        for i in list_return.values():
            str_return += i

        return str_return
        
    except Exception as e:
        return f"Error: {e}"

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')