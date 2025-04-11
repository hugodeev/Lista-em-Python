
def main():

   numeros = []
   pares = []
   impares = []

   print("Digite 20 números inteiros:")
   for i in range(20):
       num = int(input(f"Número {i + 1}: "))
       numeros.append(num)

       if num % 2 == 0:
           pares.append(num)
       else:
           impares.append(num)

   print("\nVetor completo: ", numeros)
   print("Vetor de números pares: ", pares)
   print("Vetor de números ímpares: ", impares)

if __name__ == "__main__":
   main()