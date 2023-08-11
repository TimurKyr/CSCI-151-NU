x, y = 0, 0
s = input()
for i in s:
    if i.isdigit():
        x = x + 1
    if i.isupper():
        y = y + 1
    print(f"{y} capital letters found")
    print(f"{x} capital letters found")
