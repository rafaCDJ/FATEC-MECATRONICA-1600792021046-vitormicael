#informe o valor dos lados
lado1 = int(input('Lado 1:'))
lado2 = int(input('Lado 2:'))
lado3 = int(input('Lado 3:'))
#primeiro método
if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
  if (lado1+lado2) > lado3 and (lado2+lado3) > lado1 and (lado1 + lado3) > lado2:
    print('Pode formar um trinagulo!')
#segundo método
if (lado1 > 0) and (lado2 > 0) and (lado3 > 0) and (lado1+lado2) > lado3 and (lado2+lado3) > lado1 and (lado1 + lado3) > lado2:
  print('Pode formar um trinagulo!')
