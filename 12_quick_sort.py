def merge_sort(lista):

    """

       ALGORITIMO DE ORIENTAÇÃO MERGE SORT

 

       No processo de ordenação, esse algoritmo "desmonta"

       a lista original, contendo N elementosm atê obter

       N listas com apenas um elemento cada uma. Em seguida

       usando a técnica de mesclagem (merging), "remonta a lista

       desta vez com os elementos já em ordem".

    """

    # PARTE 1: DIVISÃO DA LISTA EM LISTAS MENORES

 

    # Para que possa haver divisão da lista, esta deve ter

    # mais de um elemento

    if len(lista) > 1:

 

        # Encontra a posição do meio da lista, para fazer a divisão

        # em duas metades

        meio = len(lista) // 2

 

        # Tira uma cópia da primeira metade da lista

        sublista_esq = lista[:meio]

        # Tira uma cópia da segunda metade da lista

        sublista_dir = lista [meio:]

 

        # Chamamos recursivamente a própria função

        # continue repartindo cada sublista em duas partes menores

        sublista_esq = merge_sort(sublista_esq)

        sublista_dir = merge_sort(sublista_dir)

 

        # PARTE 2: REMONTAGEM DA LISTA, ORDENAMENTE

 

        pos_esq = pos_dir = 0

        ordenada = [] # lista vazia

 

        # Compara os elementos das sublistas entre si e insere

        # na lista ordenada  a menor dentre dois elementos

        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):

           

            # o menor elementa está na sublista da esquerda

            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:

                # "Desce" o elemento da esquerda para a lista ordenada

                ordenada.append(sublista_esq[pos_esq])

                pos_esq += 1 # Incrementa a posição da esquerda

               

            # O menor elementa está na sublista da direita

            else:

                # "Desce" o elemento da direita para a lista ordenada

                ordenada.append(sublista_dir[sublista_dir])

                pos_dir += 1 # INcrementa a posição da direita

 

         # Verificação da sobra

         sobra = []

       

        # Sobra á esquerda

        if(pos_esq < pos_dir): sobra = sublista_esq[pos_esq:]

        # Sobra á direita

        else: sobra = sublista_dir[pos_dir:]

 

        # O Resultado final é a junção (concatenação) da lista

        # ordenada com a sombra

        return ordenada + sobra