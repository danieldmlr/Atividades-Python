CNPJ = int(input('Informe o CNPJ do cliente: '))
#Se a taxa i for ao ano, o tempo t deve ser reduzido à unidade de ano;
#Caso a taxa i for ao mês, o tempo t deve ser reduzido a unidade de mês;
#Se a taxa i for ao dia, o tempo t deve ser reduzido a unidade de dia.
C = float(input('Informe a quantidade de capital: '))
i = float(input('Informe a taxa a ser calculada: '))
t = float(input('Informe o tempo a ser calculado: '))
J = (C*i*t)/ 100
M = C + J
print('O CNPJ do cliente é:', CNPJ)
print ('O valor do juros simples é:', "%.2f" % J, 'e o valor do montante é:', "%.2f" % M)
