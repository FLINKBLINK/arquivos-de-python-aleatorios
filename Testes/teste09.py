frase = 'Curso em Video Python'
print(frase)
print(frase[9])
print(frase[9 : 13])
print(frase[9 : 21])
print(frase[9 : 21 : 2])
print(frase[: 5])
print(frase[15 :])
print(frase[9 :: 3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase))


print('-' * 30)


print("""eu sou um boboca
eu sou um boboca
eu sou um boboca
eu sou um boboca
eu sou um boboca""")


print('-' * 30)


frase2 = '   Aprendo Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
