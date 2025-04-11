def contar_consoantes():

   vetor = []
  
   for i in range(10):
       caractere = input(f"Digite o {i+1}º caractere: ")
       vetor.append(caractere.lower()) 

   consoantes = "bcdfghjklmnpqrstvwxyz"
  
   consoantes_lidas = []
   for caractere in vetor:
       if caractere in consoantes:
           consoantes_lidas.append(caractere)

   print(f"\nQuantidade de consoantes lidas: {len(consoantes_lidas)}")
   print("Consoantes lidas:", consoantes_lidas)

contar_consoantes()