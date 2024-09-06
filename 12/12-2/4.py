from random import randrange

tickets = set()
while len(tickets) != 100:
    tickets.add(randrange(1000000, 10000000))
print(*tickets, sep='\n')
