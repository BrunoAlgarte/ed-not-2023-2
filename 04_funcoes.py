#Lista de frutas 
frutas = ["Laranja", "maça", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer uma lista e exibir apenas seus elementos,
# usamos a estrutura for .. in, como já vimos no arquivo nº 02
for f in frutas:
    print(f)

print("-" * 40)

# Imprimindo uma lista de trás , para frante: reversed()
for x in reversed(frutas):
    print(x)

print("-" * 40)

#No entando, frequentement precisamos exibir, além do valor do elemento, também sua poisção.
#Nesse caso, devemos usar a estrutura for..in combinada com as funções range() e len()
for pos in range(len(frutas)):
    # print(frutas[pos],".",pos)
    #  print("A fruta", frutas[pos],"está na posição", pos ,".")
    print(f"A fruta {frutas[pos]} está na posição {pos}.")

print("-" * 40)

# Ás vezes é necessário percorrer a lista de trás para frente,
# mas tendo acesso também posição dos elementos.
# Para isso, usamos a estrutura for .. in range() com três parâmetros e len()
for i in range(len(frutas) -1, -1, -1):
    print("A fruta {frutas[i]} está na posição ")