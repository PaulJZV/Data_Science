dias = ['Lunes', 'Martes','Miercoles', 'Jueves', 'Viernes']

#Agregar datos
dias.append('Sabado')
dias.append('Domingo')

#Eliminar datos 
dias.pop(2)
del dias[0:2]

#Actualizar datos
#dias[-1] = 'Lunes'

for dia in dias:
    print(dia)