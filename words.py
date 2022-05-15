'''Задание 1'''
def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return(one+delimiter+two)

words = get_summ('Leran','Python').upper()
print(words)