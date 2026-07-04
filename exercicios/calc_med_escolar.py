nota_1 = float(input('nota 1: '))
nota_2 = float(input('nota 2: '))
nota_3 = float(input('nota 3: '))

media = (nota_1 + nota_2 + nota_3) / 3
media = round(media,2)

print('Média Final: ' + str(media) )

if media >= 7:
    print('APROVADO')

elif media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
