def coords(a, b, c):
    x = -(b / (2 * a))
    y = (4 * a * c - b ** 2) / (4 * a)
    return x, y


result = coords(int(input()), int(input()), int(input()))
print(result)
