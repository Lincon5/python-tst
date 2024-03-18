#Faça um program que leia a largura e a altura de uma parede em metros, calculçe a sua área ea quantidade de tinta necessário para pintá-la, sabendo que cada litro pinta uma área de 2m2.
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área de {}m².'.format( larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
