n = input('Numerador: ')
d = input('Denominador: ')

try:
    ans = int(n) / int(d)
except ZeroDivisionError:
    print('Não pode ser dividido por zero.')
except ValueError:
    print('Você não pode usar letras.')
else:
    print(ans)
