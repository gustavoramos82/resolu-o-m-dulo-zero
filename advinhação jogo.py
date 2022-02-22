from random import randint

num_ale = randint(0,10)
num_usu = int(input('Advinha em um número que pensei entre 0 e 10:'))

if num_ale == num_usu:
    print(f'Você ganhou, eu pensei no numero {num_ale}.')
else:
    print(f'Vocẽ perdeu, pensei no número {num_ale} e vocẽ digitou {num_usu}')