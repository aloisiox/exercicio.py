a = int(input('Digite um numero: '))

def soma(a):
    if a == 0:
        return 0
    else:
        return a + soma(a-1)
resultado = soma(a)

print(f'a soma {a} é {resultado}')