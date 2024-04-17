#

print('='*35)
print('    \033[35m10 TERMOS DA PA.\033[m')
print('='*35)

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo, razão):
    print('{}'.format(c), end='->')
print('Acabou.')