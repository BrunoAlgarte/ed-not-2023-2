# LISTAS
# Listas são uma forma de armazear mais de um valor em uma
# única variável. Os valores podem ser de tipos diferentes;

# Uma lista de números
valores = [2, 3, 5, 7, 9, 11]

# Uma lista com valores de tipos variados
mix = ["batata", 1.25, True, "tomate", 44]

# Lista de strings
legumes = ["batata", "tomate", "abrobrinha", "cenoura"]

# OPERAÇÔES SOBRE LISTAS

# 1) PERCURSO: significa percorrer a lista do primeiro ao
#              ultimo elemento, fazendo alg com cada um deles.

# Imprimindo cada um dos elementos da lista, um por linha:
for val in valores:
    print(val)

print("-"*40)

# Imprimindo o dobro do valor de cada elementa da lista
for x in valores:
    print(x*2)

print("-"*40)

# 2) INSERINDO UM NOVO ELEMENTO NO *FIM* DA LISTA

valores.append(13)
legumes.append("cebola")

print(valores)
print(legumes)

print("-"*40)

# 3) INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÂO ESPECIFICADA
#    Parãmetros:
#    1º: a posição onde sera inserido o novo elemento
#    2º: o novo elemento a ser inserido

legumes.insert(2, "mandioquinha")
print(legumes)
legumes.insert(0, "beterraba")
print(legumes)

print("-"*40)

#4) ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECIFICA
print("Elemento na QUARTA posição:", valores[3])
print("Elemento na PRIMEIRA posição:", valores[0])
print("Elemento na ÚLTIMA posição:", valores[-1])
print("Elemento na PENÚLTIMA posição:", valores[-2])

print("-"*40)

# 5) SUBSTITUINDO VALORES EXISTENTES

print("ANTES: ", legumes)

# Substituindo o valor da posição 3

# Substituindo o valor da posição 3
legumes[3] = "vagem"
# Substituindo o valor da posição 0
legumes[0] = "mandioca"
# Substituindo o valor da última posição
legumes[-1] = "milho"

print("DEPOIS: ", legumes)

print("-"*40)

# 6) DETERMINANDO A QUANTIDADE DE ELEMENTOS NA LISTA: len()
print("Número de elemntos ns lista de valores ", len(valores))
print("Número de elemntos ns lista de valores ", len(legumes))

print("-"*40)
 
#7) REMOVENDO O ULTIMO ELEMENTO DE UMA LISTA: pop()
print("ANTES ", valores)
removido = valores.pop()
print("Valo removido: ", removido)
print("DEPOIS:", valores)

print("-"*40)

#8 REMOVENDO UM ELEMNTO POR SUA POSIÇÃO: pop () com parâmetro
removido = valores.pop(3)
print("Valor removido da posição3: ", removido )
print(valores)
removido = valores.pop(0)
print("Valor removido da primeira posição: ", removido)
print(valores)

print("-"*40)

# 9) REMOVENDO UM ELEMENTO PELO SEU VALOR: remove()
print("ANTES: ", legumes)
legumes.remove("abrobrinha")
print(" APÓS REMOÇÃO DE ABROBRINHA: ", legumes)

print("-"*40)

# Acrescwntando alguns lagumes para aumentar a lista
legumes.append("beterraba")
legumes.append("abrobrinha")
legumes.append("batata doce")
legumes.append("mandioquinha")
legumes.append("cará")
legumes.append("nabo")

#10) FATIANDO UMA LISTA
# Fatiar significa copiar uma parte da lista (um sulista) oara uma nova lista
#

print(legumes)

# Criar uma sublista que contém os elemtnos da posição 2 até a posição 7
# (posição 8 NÂO entra)
sublista2_7 = legumes [2:8]
print("Sublista de 2 a 7: ", sublista2_7)

# Cria uma sublista que contém os elemtnos do início até a posição 5
# (posição 6 NÃO entra)
sublista0_5 = legumes[:6]
print("Sublista de 0 a 5: ", sublista0_5)

# Cria uma sublista que contém os elemtnos da posição 8
sublista8_fim = legumes[8:]
print("Sublista de 8 até o fim: ", sublista8_fim)