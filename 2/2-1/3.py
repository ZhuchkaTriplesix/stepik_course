x = input()
a = len(x)
full = a * 60
ruble = full // 100
demi = full - (ruble * 100)
print(f"{ruble} р. {demi} коп.")
