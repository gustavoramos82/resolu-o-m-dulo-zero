#Colocando a data atual
from datetime import date
data_atual = date.today()
ano_atual = data_atual.year

#colocando a data da pessoa e idade
ano_pessoal = int(input('Digite o seu ano de nascimento:'))
idade = ano_atual - ano_pessoal
#Fazendo o cálculo
if idade < 16 :
    print(f'Você tem {idade} anos e tem voto negado.')
elif idade >= 16 and idade < 18:
    print(f'Vocẽ tem {idade} e o seu voto é opcional.')
elif idade >=18:
    print(f'Você tem {idade} e o seu voto é obrigatório.')