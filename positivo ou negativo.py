num = int(input('informe o número:'))

while num == 0:
    print('O zero nem um núro positivo ou negativo, por favor, tente novamente.')
    num = int(input('informe o número:'))

if num < 0:
    print(f'O número {num} é negativo.')
else:
    print(f'O número {num} é positivo.')