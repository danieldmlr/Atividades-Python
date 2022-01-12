CNPJ = int(input('Informe o CNPJ do cliente: '))
#Se a taxa i for ao ano, o tempo t deve ser reduzido à unidade de ano;
#Caso a taxa i for ao mês, o tempo t deve ser reduzido a unidade de mês;
#Se a taxa i for ao dia, o tempo t deve ser reduzido a unidade de dia.
C = float(input('Informe a quantidade de capital: '))
i = float(input('Informe a taxa a ser calculada: '))/100
t = float(input('Informe o tempo a ser calculado: '))
M = C * ((1 + i)**t)
J = M - C
print('O CPF do cliente é:', CPF)
print ('o valor do montante com juros compostos após o tempo determinado é:', "%.2f" % M, 'e o valor do juros total é:', "%.2f" % J)
