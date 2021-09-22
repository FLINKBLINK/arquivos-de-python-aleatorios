dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos quilônetros o carro rodou? '))
pago = (dias * 60) + (km * 0.15)
print('O valor total a pagar pelo aluguel do carro é de R${:.2f}'.format(pago))