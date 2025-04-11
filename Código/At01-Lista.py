n = int(input("Quantos números serão lidos? "))

while n <= 0:
   print("Por favor, insira um número maior que zero.")
   n = int(input("Quantos números serão lidos? "))

numeros = []

print("Digite os números:")
for i in range(n):
   while True:
       try:
           num = int(input(f"Digite o número {i + 1}: "))
           numeros.append(num)
           break
       except ValueError:
           print("Por favor, insira um número válido.")

x = int(input("Qual número deseja procurar? "))
if x in numeros:
   print(f"{x} pertence à lista.")
else:
   print(f"{x} não pertence à lista")
   