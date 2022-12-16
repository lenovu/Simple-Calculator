
def main():
    while True:
        a = float(input('''
Which operator do you wish to choose? (Type a number...)
|1. (+)| |2. (-)| |3. (/)| |4. (*)|
'''))
        b = float(input('Input the 1. number: '))
        c = float(input('Input the 2. number: '))

        if a == 1:
            x = b + c
            return print(f'{b} + {c} = {x}')
        elif a == 2:
            x = b - c
            return print(f'{b} - {c} = {x}')
        elif a == 3:
            x = b / c
            return print(f'{b} / {c} = {x}')
        elif a == 4:
            x = b * c
            return print(f'{b} * {c} = {x}')
        else:
            i = input('''
Invalid input!
Would you like to try again?:
''')
            i = i.lower()
            if i == 'yes' or 'y':
                continue
            if i == 'no' or 'n':
                exit()
main()





