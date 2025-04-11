vetor = []

try:
    
  for i in range(5):
    num = int(input(f'Digite seu {i + 1}° número:'))
    vetor.append(num)

  print(f'Seus 5 números são: {vetor}')

except ValueError:
    print(f'Número invalido, tente novamente!')
