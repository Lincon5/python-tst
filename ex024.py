# Crie um programa que leia o nome de uma cidade, e diga se ela começa ou não com nome 'Santos'.

cid = str(input('\033[0;37mQual cidade você nasceu?\033[m')).strip()
print(cid[:5].upper() =='SANTO')