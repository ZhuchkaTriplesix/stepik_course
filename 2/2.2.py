a = float(input())
b = float(input())
c = a / b ** 2
if c < 18.5:
    print("Недостаточная масса")
elif c > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")
