vetor = []

try:
    n = int(input(f'Quantos números serão adicionados:'))

    for i in range(n):
        num = int(input(f'Digite o {i + 1}° número:'))
        vetor.append(num)

    soma = sum(vetor)
    print(f'Soma total: {soma}')

except ValueError:
        print(f'Somente número Inteiros!!')