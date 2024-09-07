with open('goats.txt', 'r', encoding='utf-8') as file, open('answer.txt', 'w', encoding='utf-8') as answer:
    lst = []
    for string in file.read().split('GOATS'):
        lst.append(string.strip('COLOURS').strip('\n').strip(' goat ').split(' goat\n'))
    for c in lst[0]:
        if lst[1].count(c) > len(lst[1]) * 0.07:
            print(f'{c} goat', file=answer)
