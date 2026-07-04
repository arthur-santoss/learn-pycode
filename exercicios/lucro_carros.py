valor_pago = float(input('valor pago: '))
valor_investido = float(input('valor investido: '))
valor_venda = float(input('valor venda: '))

custo_total = valor_pago + valor_investido
lucro = valor_venda - custo_total

print('Custo total: R$ ' + str(custo_total))
print('Lucro obtido: R$ ' + str(lucro))

if lucro > 0:
    print('Lucro na venda')
elif lucro < 0:
    print('Prejuíso na venda')
else:
    print('Vendido à preço de custo')
