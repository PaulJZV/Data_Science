# Las tuplas son inmutables

dias = ('Lunes', 'Martes','Miercoles', 'Jueves', 'Viernes')
print(f'El tipo de dato original: {type(dias)}')
dias = list(dias)
print(f'El tipo de dato modificado: {type(dias)}')
dias.append('Sabado')
dias = tuple(dias)
print(dias)