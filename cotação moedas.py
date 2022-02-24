import requests as re 
from fractions import Fraction

requi = re.get('https://economia.awesomeapi.com.br/json/all')
requi_chile = re.get('https://economia.awesomeapi.com.br/json/last/CLP-BRL')
requi_dic = requi.json()
requi_dic2 = requi_chile.json()

cota_dolar = requi_dic['USD']['bid']
cota_euro = requi_dic['EUR']['bid']
cota_libra_esterlina = requi_dic['GBP']['bid']
cota_dolar_canadense = requi_dic['CAD']['bid']
cota_peso_argentino = requi_dic['ARS']['bid']
cota_peso_chileno = requi_dic2['CLPBRL']['bid']

moeda_converter = int(input('''Para qual valor você desejar conveter (digite de acordo com as opções):
1- Dolar, 2 - Euro, 3 - Libra Esterlina, 4- Dólar Canadense, 5 - Peso Argentino, 6 - Peso Chileno? '''))

valor = float(input('Digite o valor que gostaria de converter: R$'))

conv_dolar = float(Fraction(valor)/Fraction(cota_dolar))
conv_euro = float(Fraction(valor)/Fraction(cota_euro))
conv_libra_esterlina = float(Fraction(valor)/Fraction(cota_libra_esterlina))
conv_dolar_canadense = float(Fraction(valor)/Fraction(cota_dolar_canadense))
conv_peso_argentino = float(Fraction(valor)/Fraction(cota_peso_argentino))
conv_peso_chileno = float(Fraction(valor)/Fraction(cota_peso_chileno))

if moeda_converter == 1:
    print(f'{valor:.2f} reais equivale a {conv_dolar:.2f} dólares.')
elif moeda_converter == 2:
    print(f'{valor:.2f} reais equivale a {conv_euro:.2f} euros.')
elif moeda_converter == 3:
    print(f'{valor:.2f} reais equivale a {conv_libra_esterlina:.2f} libras esterlinas.')
elif moeda_converter == 4:
    print(f'{valor:.2f} reais equivale a {conv_dolar_canadense:.2f} dolares canadenses.')
elif moeda_converter == 5:
    print(f'{valor:.2f} reais equivale a {conv_peso_argentino:.2f} pesos argentinos.')
elif moeda_converter == 6:
    print(f'{valor:.2f} reais equivale a {conv_peso_chileno:.2f} pesos chilenos.')