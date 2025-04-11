lista = []

try:

    n = int(input('Quantos números serão adicionados:'))

    for i in range(n):
     lista.append(int(input(f'Digite seu {i + 1}° número:')))

    x = int(input(f'Qual número você quer remover:'))


    if x in lista:
     lista.remove(x)
     print(f'Número {x} removido da lista!')

    else: 
        print(f'Número {x} não existe na lista!')

        print('Lista final:', lista)


except ValueError:
    print('Por favor, digite apenas números inteiros.')
    

