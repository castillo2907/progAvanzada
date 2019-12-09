## Ejercicio 82
#En la ciudad de mexico la taria fe taxi uber consiste en un precio base de $44 pesos mas $12 pesos por cada kilometro recorrido
#Escriba una funcion que tome la distancia viajada (en km)
#El cual debe ser el unico argumento y regrese la tarifa total como resultado.
#Escriba un programa principal que demuestre la funcion 
def tarifa (distancia):
    total = 44.00 + distancia*12.00
    return total
km = float(input('Inserta los km recorridos: '))

cuota = tarifa(km)
print('la tarifa total es: ',cuota)


