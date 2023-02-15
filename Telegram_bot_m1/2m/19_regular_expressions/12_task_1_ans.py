import re

with open('kolobok.txt', 'r', encoding="utf-8") as file:
    f = file.read()

kolobok = re.findall(r'колобок', f, re.I)
print(kolobok)
print(len(kolobok))
