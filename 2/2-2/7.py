a = input()
b = input()

if a == "камень" and b == "ножницы":
    print("Тимур")
elif a == "ножницы" and b == "бумага":
    print("Тимур")
elif a == "бумага" and b == "камень":
    print("Тимур")
elif a == b:
    print("ничья")
else:
    print("Руслан")
