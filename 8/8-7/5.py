set_1, set_2, set_3 = (set(input().split()) for _ in range(3))
print(*(sorted(set_3 - (set_1 | set_2), key=int, reverse=True)))
