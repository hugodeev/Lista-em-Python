vetor = []

try:

    for i in range(10):
        num = float(input(f'Digite seu {i + 1}° número:'))
        vetor.append(num)

    print("\nOs números na ordem inversa são:")

    for num in reversed(vetor):
     print(num)

except ValueError:
    print(f'Somente número Inteiros!!')