from random import shuffle
nome1 = input('Digite o nome do(a) primeiro aluno(a): ')
nome2 = input('Digite o nome do(a) segundo aluno(a): ')
nome3 = input('Digite o nome do(a) terceiro aluno(a): ')
nome4 = input('Digite o nome do(a) quarto aluno(a): ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem escolhida para a apresentação dos trabalhos foi: ')
print(lista)
