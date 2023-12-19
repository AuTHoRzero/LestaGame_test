from typing import Union

def isEven_main(value): 
    '''
    Первоначальный вариант
    '''
    return value % 2 == 0 

def isEven(n: Union[int, str]) -> bool:
    '''
    В этом варианте, функция не проводит вычисления, а лишь проверяет,
    что число n оканчивается на 0 2 4 6 8, что является признаком деления на 2.
    Данный вариант не учитывает, что число n может быть представлено в виде
    дробного числа или оно является 0.

    В сравнении с приведённым в задании примером, данная функция может работать как со строками, так и с целыми числами,
    но не может работать с числами, с плавающей точкой.
    '''
    return str(n)[-1] in '02468'

def isEven2(n: Union[int, float, str]) -> bool:
    '''
    Данный вариант позволяет учитывать, что число n может равняться 0
    или иметь тип float
    '''
    if n != 0:
        prepare = str(n)
        if prepare.__contains__('.'):
            return prepare.split('.')[1] == '0' and prepare.split('.')[0][-1] in '02468'

        return prepare[-1] in '02468'
    return False