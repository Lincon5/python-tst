# Crie um programa que leia o nome de uma cidade, e diga se ela começa ou não com nome 'Santos'.

cid = str(input('Qual cidade você nasceu?')).strip()
print(cid[:5].upper() =='SANTO')