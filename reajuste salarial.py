salario = float(input('Qual o valor do salário? R$'))

if salario <= 280:
    print(f'Seu salário era R${salario}.')
    print('teve um aumento de 20%.')
    print(f'O valor do aumento foi de R${salario*0.2}')
    print(f'Seu novo salário é de R${salario+salario*0.2}')
elif salario > 280 and salario <= 700:
    print(f'Seu salário era R${salario}.')
    print('teve um aumento de 15%.')
    print(f'O valor do aumento foi de R${salario*0.15}')
    print(f'Seu novo salário é de R${salario+salario*0.15}')
elif salario > 700 and salario < 1500:
    print(f'Seu salário era R${salario}.')
    print('teve um aumento de 10%.')
    print(f'O valor do aumento foi de R${salario*0.1}')
    print(f'Seu novo salário é de R${salario+salario*0.1}')
elif salario <= 1500:
    print(f'Seu salário era R${salario}.')
    print('teve um aumento de 5%.')
    print(f'O valor do aumento foi de R${salario*0.05}')
    print(f'Seu novo salário é de R${salario+salario*0.05}')