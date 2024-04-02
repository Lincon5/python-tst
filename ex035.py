# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[0;31m-=\033[m' *25 )
print('\033[1;35mAnalisador de Triângulos.\033[m')
print('\033[0;31m-=\033[m' *25)
l1 = float(input('Primeiro segmento:'))
l2 = float(input('Segundo segmento:'))
l3 = float(input('Terceiro segmento:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: # operação matemática.
    print('Eles podem formar um triângulo, \033[0;34mparabéns\033[m.')
else:
    print('Os valores digitado não podem, formar um triângulo, \033[0;31mque pena\033[m.')