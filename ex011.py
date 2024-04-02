#Faça um program que leia a largura e a altura de uma parede em metros, calculçe a sua área ea quantidade de tinta necessário para pintá-la, sabendo que cada litro pinta uma área de 2m2.
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área de {}m².'.format( larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de \033[0;34m{}\033[ml de tinta.'.format(tinta))


# ANSI:códigos de escape sequence ANSI para configurar cores para os seus programas em Python.
# Melhores funções para utilizar em python:
# STYLE:  0 = none / 1 = bold / 4 = underline e 7 = negative.
# TEXT: cores: 30=Branco / 31=Vermelho / 32=Verde / 33=Amarelo / 34=Azul / 35=roxo / 36=verde água / 37=Cinza. Cores de letra começa com 3.
# BACK: Cores:40=Branco / 41=Vermelho / 42=Verde / 43=Amarelo / 44=Azul / 45=roxo / 46=verde água / 47=Cinza. Cores de fundo começa com 4.
# Código a ser usado: \033[0;33;33m ou no .format()= {}{}{}.format('\033[0;31m' , nome, '\033[m')
