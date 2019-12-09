#Ejercicio 83
#Amazon probee envio expres para muchos de sus prodcutos a un costo de $195 pesos por el primer producto
# y de $29.50 para cada producto subsecuente
#Escriba una funcion que tome el numero de productos como su unico argumento.
#Regrese el costo de envio total como el resultado de la funcion.
#Incluya un programa principal que lea el numero de productos comprados por el usuario y que desplieje el costo total de envio.

def envio (productos):
    if productos == 1:
        total = 195.00
    
    else:
        total= (195.00 + (productos-1) * 29.50)

    return total
produ = float(input('Inserte el total de productos: '))

producto = envio(produ)
print('la tarifa total es: ',producto)