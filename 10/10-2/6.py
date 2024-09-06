original_map = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' ',
}
work_map = {letter: number * indx
            for number, string in original_map.items()
            for indx, letter in enumerate(string, 1)}

input_string = input().upper()

for letter in input_string:
    print(work_map.get(letter, ''), end='')
