altura=int(input("Digite altura: "))
ancho=int(input("Digite ancho: "))
area=altura*ancho
perimetro=(altura*2)+(ancho*2)

print(f'El area es: {area}')
print(f'El perimetro es: {perimetro}')

for i in range (1,altura+1):
    for j in range (1,ancho+1):
        print("*", end="")
    print(" ")