saque = int(input('Qual é o valor do saque:'))
valor = saque
quant_100 = quant_50 = quant_10 = quant_5 = quant_1 = 0

while saque !=0 :
    if saque >= 100:
        quant_100 = saque//100
        saque = saque%100
    elif saque < 100 and saque >=50:
        quant_50 = saque//50
        saque = saque%50
    elif saque < 50 and saque >= 10:
        quant_10 = saque//10
        saque = saque%10
    elif saque < 10 and saque >=5:
        quant_5 = saque//5
        saque = saque%5
    elif saque < 5:
        quant_1 = int(saque/1)
        saque = 0
    
    if saque == 0:
        break

print(f'Para sacar R${valor}, vai ser fornecido:')
print(f'Vão ser fornecidos {quant_100} notas de R$ 100, {quant_50} notas de R$ 50,')
print(f'{quant_10} notas de R$ 10, {quant_5} notas de R$ 5 e {quant_1} notas de 1 real')