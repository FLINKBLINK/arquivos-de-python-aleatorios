nome = input('Digite o nome do(a) aluno(a) ao qual as notas vão ser atribuidas: ')
nota1 = float(input('Digite a nota 01: '))
nota2 = float(input('Digite a nota 02: '))
media = (nota1 + nota2) / 2
print('A média do(a) aluno(a) {} foi de {:.1f}'.format(nome, media))
