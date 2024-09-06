timur = input()
ruslan = input()
result = {'камень': ['ножницы', 'ящерица'],
          'ножницы': ['бумага', 'ящерица'],
          'бумага': ['камень', 'Спок'],
          'Спок': ['ножницы', 'камень'],
          'ящерица': ['бумага', 'Спок']}
if timur == ruslan:
    print('ничья')
else:
    if ruslan in result[timur]:
        print('Тимур')
    else:
        print('Руслан')
