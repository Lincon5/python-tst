# Faça um algoriiitmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input("Qual é o preço do produto? R$"))
novo = preço - (preço * 5 / 100)
d = novo - preço
print("O produto que custava R${:.2f}, na promioção com desconto de 5% vaii sair a R${:.2f}".format(preço, novo))


