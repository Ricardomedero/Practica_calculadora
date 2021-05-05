
print("Bienvenidos a mi caculadora!!!\n1. Suma\n2. Resta\n3. Multiplicacion\n4. division\n5. comparador")


s = input("elija la operacion que desea realizar:  ")

if s.isnumeric():

    x = float(input("ingrese el primer numero: "))

    if int(s) in range(1,6):
        y= float(input("ingrese el segundo numero: "))

        if int(s) == 1:
    

         print(f"{x} + {y} = {x+y}")

else:
    print("error entrada invalida")