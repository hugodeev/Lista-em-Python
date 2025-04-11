
notas = []

for i in range(4):
   nota = float(input(f"Digite a {i+1}ª nota: "))
   notas.append(nota)


media = sum(notas) / len(notas)


print("\nAs notas são:")
for nota in notas:
   print(nota)


print(f"\nA média das notas é: {media:.2f}")


if media >= 70:
   print('Você foi aprovado!!')


else:
   print('Você foi reprovado!!')

