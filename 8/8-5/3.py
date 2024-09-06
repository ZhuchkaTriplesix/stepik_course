import re

text = re.sub(r'[.,;:-?-!]', '', input().lower())
words_list = text.split()
print(len(set(words_list)))
