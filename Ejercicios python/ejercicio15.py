n1=int(input("numero 1"))
n2=int(input("numero 2"))
n3=int(input("numero 3"))

if n1>n2:
    if n1>n3:
        print(n1)
    else:
        print(n3)
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)