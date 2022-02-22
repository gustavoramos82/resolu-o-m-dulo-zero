# Recebendo o valor
valor = float(input('Qual é o valor final da refeição? R$'))

#Recebendo a taxa
taxa = float(input('Quanto é a taxa de serviço? (em %)'))

#Calculandfo o valor total
valor_total = (valor*taxa)/100 + valor

print(f'O valor total é de R${valor_total}')