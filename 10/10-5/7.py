words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {word: [ord(w) for w in word] for word in words}
