li = [word.strip(".,!?:;-").lower() for word in input().split()]
di = {word: li.count(word) for word in li}
m = min(di.values())

for k, v in sorted(di.items(), key=lambda t: t[0]):
    if v == m:
        print(k)
        break
