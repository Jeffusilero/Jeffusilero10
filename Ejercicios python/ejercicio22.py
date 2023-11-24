"""Se ingresan por teclado tres números, si todos los valores 
ingresados son menores a 10, imprimir en pantalla la leyenda 
"Todos los números son menores a diez"."""

n1= int(input("numero 1 "))
n2= int(input("numero 2 "))
n3= int(input("numero 3 "))

if n1<10 and n2<10 and n3<10:
    print("Todos los numero son menores a diez")
