# range() é uma função que gera uma faixa de números. 
# É muito usada em associação com listas.

#1) range() com 1 parãmetro: gera uma faixa que vai de 
# 0 (zero) até o valor do paâmetro -1
for num in range(10):
    print(num)

# 2) range() com 2 parâmetros: gera uma sequência começando
# pelo primeiro parâmetro (inclusive) e indo até
# o valor do segundo parâmetro (eclusive, NÃO ENTRA)
for i in range(10,15):
    print(i)

print("-"*40)

# 3) range() com 3 parâmetros:
#   1º: limite inferior (invlusive)
#   2º: limite superior (exclusive, NÃo ENTRA)
#   3º: passo (de quanto em quanto a sequência vai saltar; PODE SER NEGATIVO)
for i in range(1,22, 3): #De 1 a 21 saltando de 3 em 3
    print(i)

print("-"*40)

# 4) range() com passo negativo
for i in range(10,0, -1): #Contagem regressiva de 10 a 1
    print(i)