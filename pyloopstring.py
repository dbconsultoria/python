str = '365 dias de Python!'
strdigit = ''

for n in reversed(str):
    if n.isdigit():
        strdigit += n

print(strdigit)