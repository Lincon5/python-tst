# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

nome = str(input('Qual é seu nome?'))
salário = float(input('Qual é o seu salário R$?'))
if salário <= 1250:
    novo = salário + (salário * 30 / 100 )
else:
    novo = salário + (salário * 20 / 100)
print(' Oi {},o seu  salário que era {:.2f}, depois da ITIL vai ser  {:.2f}.'.format(nome,salário,novo))

