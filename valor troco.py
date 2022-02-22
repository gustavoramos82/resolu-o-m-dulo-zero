valor_compra = float(input('Quanto custou o valor da compra? R$'))
valor_cliente = float(input('Quanto recebeu do cliente? R$'))

if valor_compra == valor_cliente:
    print('Está certo, não precisa de troco.')
elif valor_compra < valor_cliente:
    valor_total = valor_cliente-valor_compra
    print(f'O troco é de R${valor_total}')
else:
    falta = valor_compra - valor_cliente
    print(f'Esse dinheiro não vai pagar a compra, aind a precisa pagar R${falta}')