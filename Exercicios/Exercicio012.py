preco = float(input('Digite o preço do produto: '))
desc = preco - (preco / 100) * 5
print('O preço do produto com o desconto de 5%'+' ficou {:.2f}'.format(desc))
