def com(n):
    return 0.5 ** (n[0] ** 2 + n[1] ** 2)


points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
points.sort(key=com, reverse=True)
print(points)
