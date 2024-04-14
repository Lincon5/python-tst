# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0 # acumulador
cont = 0 # contador
for n in range(1, 501, 2):
    if n % 3 ==0:
        cont = cont + 1
        soma = soma + n
print('A soma de todos os {} valores é {} '.format(cont, soma))

# jeito simplificado.
#soma = 0 # acumulador
#cont = 0 # contador
#for n in range(1, 501, 2):
#   if n % 3 ==0:
#        cont += 1
#        soma += n
#print('A soma de todos os {} valores é {} '.format(cont, soma))