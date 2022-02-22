from ast import In
from random import randint
num_ale = randint(1,3)

# pedra = 1, papel = 2 e tesoura = 3

rodadas = int(input('Quantas rodadas vc deseja jogar?'))
perdeu =  n_rod = ganhou = empate = 0

cont = 'S'

while cont in "Ss":
    for n in range (1,rodadas+1):
        n_rod = n_rod + 1
        num_usu = int(input('Digite o que vai querer, 1 para pedra, 2 para papel e 3 para tesoura '))
        
        if num_usu == 1 and num_ale == 3:
            print('Você ganhou, eu escolhi tesoura e vocẽ pedra.')
            ganhou = ganhou + 1
            num_ale = randint(1,3)
        elif num_usu == 3 and num_ale == 1:
            print('Vocẽ perdeu, eu escolhi pedra e vc tesoura.')
            perdeu = perdeu + 1
            num_ale = randint(1,3)
        elif num_usu == 3 and num_ale == 2:
            print('Você ganhou, você tirou tesoura e eu pappel.')
            ganhou = ganhou + 1
            num_ale = randint(1,3)
        elif num_usu == 2 and num_ale == 3:
            print('Vocẽ perdeu, eu escolhi tesoura e vc papel.')
            perdeu = perdeu + 1
            num_ale = randint(1,3)
        elif num_usu == 2 and num_ale == 1:
            print('Você ganhou, eu escolhi pedra e você papel ')
            ganhou = ganhou + 1
            num_ale = randint(1,3)
        elif num_usu == 1 and num_ale == 2:
            print('Você perdeu, eu escolhi papel e vocẽ pedra.')
            perdeu = perdeu + 1
            num_ale = randint(1,3)
        elif num_usu == num_ale:
            print('partida empatada, jogamos a mesma coisa.')
            empate = empate + 1
           
        
        print (f'foi a rodada {n}')

    cont = input('Deseja continuar? (S para sim e N para Não:').upper()
    
    if cont != 'S':
        break
    
    rodadas = int(input('Quantas rodadas vc deseja jogar?'))
print (f'Você jogou {n_rod} rodadas')
if ganhou > perdeu:
    print(f'Você ganhou {ganhou}, perdeu {perdeu} e empatou {empate} de {n_rod} partidas')
    print('Você é o grande campeão.')
elif ganhou == perdeu:
    print(f'Você ganhou {ganhou} partidas, perdeu {perdeu} e empatou {empate}  de {n_rod} partidas')
    print('Partida empatada.')
else:
    print(f'Você ganhou {ganhou} partidas, perdeu {perdeu} e empatou {empate}  de {n_rod} partidas')
    print('Você perdeu.')