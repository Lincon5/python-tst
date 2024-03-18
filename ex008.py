#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
media = float(input('Digite uma distância em metros:'))
dm = media * 10
cm = media * 100
mm = media * 1000
dam = media / 10
hm = media / 100
km = media / 1000

print(('A media de {}m corresponde a {}dm \n{}cm \n{}mm \n{}dm \n{}hm \n{}km'.format(media, dm, cm, mm, dm, hm, km)))

