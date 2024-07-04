#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso  esteja errado, peça a digitação nobamente até ter umm valor correto.

# .strip usado para retirar os espaços.
# .upper()[0] para transforma a letra minuscula em maiuscula, o [0] para pegar so a primeira letra.

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados inválidos. Por favor digite novamente seu sexo: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

