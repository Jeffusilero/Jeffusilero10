n1=int(input("nota 1"))
n2=int(input("nota 2"))
n3=int(input("nota 3"))
prom= (n1+n2+n3)/3

if prom>=7:
    print("Promocionado")
else:
    if prom>=4:
        print("Regular")
    else:
        print("Reprobado")