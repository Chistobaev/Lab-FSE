text = input()
x = []
j = 0
for i in range(len(text)):
    if text[i] == ' ':
        x.append(text[j:i])
        j = i + 1
x.append(text[j:])
for i in x:
    if len(i) >= 3:
        print(i[0].upper(), end='')
