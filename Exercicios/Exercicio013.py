salario = float(input('Digite o salario do seu funcionário: R$'))
aumento = ((salario / 100) * 15) + salario
print('O salário reajustado em 15% do seu funcionários ficou em R${:.2f}'.format(aumento))
