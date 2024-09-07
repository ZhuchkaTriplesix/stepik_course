a = input()

print("YES" if all(
    [any(map(lambda x: x.isdigit(), a)), any(map(lambda x: x.islower(), a)), any(map(lambda x: x.isupper(), a)),
     len(a) > 6]) else "NO")
