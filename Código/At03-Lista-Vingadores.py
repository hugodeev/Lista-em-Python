vingadores = ["Homem de Ferro", "Capitão América", "Thor", "Hulk", "Viúva Negra", "Gavião Arqueiro"]
print(f'Lista de Vingadores: {vingadores}')


vingadores.append("Homem-Aranha")


print("Vingador Thor está na posição:", vingadores.index("Thor"))


vingadores.remove("Viúva Negra")
vingadores.remove("Homem de Ferro")
print(f'Os vigadores Viúva Negra e Homem de Ferro foram mortos: {vingadores}')


desaparecidos = ["Homem de Ferro", "Viúva Negra"]
vingador_x = input("Digite o nome de um Vingador para verificar: ")

if vingador_x in vingadores:
   print(vingador_x, "é um Vingador presente.")

elif vingador_x in desaparecidos:
   print(vingador_x, "é um Vingador desaparecido.")
   
else:
   print(vingador_x, "não faz parte da Iniciativa Vingadores.")