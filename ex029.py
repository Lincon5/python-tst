# Programa para gerar multa.

velocidade = float(input('Qual é a velocidade do carro?'))
if velocidade > 60:
    print('Multado! Você passou do limite permitido, que e de 60KM/H.')
    multa = (velocidade-60) * 5
    print('Valor da sua multa é de R${:.2f}.'.format(multa))
print('Dirija com cuidaddo.')

# Esse código foi feito em uma condição simples.