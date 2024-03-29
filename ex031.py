# Programa de viagem.

# código composto.
distância: float = float(input('Qual é a distância da sua viagem?'))
print('Sua viagem de {:.2f} KM.'.format(distância))
if distância <= 200:
    preço = distância * 1.20
else:
    preço = distância * 0.60
print('Preço da sua viagem e de R${:.2f}.'.format(preço))
