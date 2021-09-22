preco = float(input('Digite o preço do produto: R$'))
desc = preco - ((preco / 100) * 5)
print('O preço do produto com o desconto de 5% ficou R${:.2f}'.format(desc))
