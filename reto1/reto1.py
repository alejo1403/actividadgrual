def llenar():

    lista=[]
    for i in range(3):
        numero=int(input("digite un nuemro"))
        lista.append(numero)
    return lista

def sumar(lista):
    suma=0
    for elemento in lista:
        suma+=elemento
    return suma


def promediar(sumatoria,cantidadTotalDatos):
    promedio=sumatoria/cantidadTotalDatos
    return promedio

datos=llenar()
sumatoria=sumar(datos)
promedio=promediar(sumatoria,len(datos))
print(f'el promedio fue: {promedio}')
