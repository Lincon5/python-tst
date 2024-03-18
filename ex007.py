#Desenvolva uma programaque leia as duas notas de um aluno,calcule e mostre a sua média.

n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
n3 = float(input('Terceira nota do aluno:'))
n4 = float(input('Quarta nota do aluno:'))
m = (n1 + n2 + n3 + n4) / 2
print('A média entre {:.1f} e {:.1F} e {:.1F} e {:.1f} é igual a {:.1f}'.format(n1, n2, n3, n4,  m))




