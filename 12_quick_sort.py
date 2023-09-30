def quick sort(lista, ini = 0, fim = None):
"""
   ALGORITMO DE ORDENAÇÃO QUICK SORT

   Escolhe um dos elementos da lista para ser o pivô (na nossa
   implementação, será o útimo elemnto) e, na primeira passada,
   divide a lista, a partir da posição final do pivô,
   em uma sublista á esquerda, contendo apenas valores menores
   que o pivô, e outra sublista á direita, que contém apenas
   valores maiores que o pivô.
   Em seguida, recursivamente, repete o processo em cada uma das
   sublistas, até que toda a lista esteja ordenada.
"""

# Quando não soubermos o valor da vatiável "fim", atribuímos a
# ela o valor da última posição da lista
if fim is None: fim = len(lista) -1

# Para que o algoritmo trabalhe, é necessário que a faixa delimitada
# pelas variáveis "ini" e "fim" tenha, pelo menos, dois elementos.
# Caso contr´rio, saímos da função sem fazer nada
if fim <= ini: return 

# Inicialização dos variáveis
pivot = fim
div = ini - 1

# Percorre a lista da posição "ini" até a posição "fim" - 1
for pos in range(ini, fim):
    # Seo elemento da posição "pos" for MENOR que o elemento da 
    # posição "pivot", executa algumas açoes
    if lista[pos] < lista[pivot]:
        div += 1 # Chega a "div" uma poisção paa a frente

        # Efetua a troca entre os elementos das posições "pos" e "div",
        # desde que essas variáveis tenham valor distindo entre si
        if pos != div and lista[pos] < lista[div:]:
            lista[pos], lista[div] = lista[div], lista[pos]

#Depois que o "Pos"  chega em sua posição final, "div" deve ser
# incrementando uma última vez
div += 1

# Caso os valores da posições "pivot" e "div" sejam dierente entre
# si, efetua a troca mútua dos elementos nessas posições, caso p
# primeiro seja menor que o segundo 
if pivot !=div and lista[pivot] < lista[div];
    lista[pivot], lista[div] = lista[div], lista[pivot]

# NESTE PONTO, O ELEMENTO DA POSIÇÃO "div" ESTÁ EM SEU LOCAL CORRETO

# Chamamos recursivamente a função para ordenar a sublista á esquerda
# da posição "div"
quick_sort(lista, ini, div -1)

# A mesma coisa, só que para sublista á direita de "div"
quick_sort(lsita, div +1, fim)

#####################################################################