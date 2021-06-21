def area(b,h):
    return b*h/2

def tipo_triangulo(l1,l2,l3):
    if l1 == l2 == l3:
        print("El triangulo es equilátero ")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")

def main():
    while True:
        opt = int(input(""" Bienvenido a la calculadora de triángulos, 
        \n este programa permite calcular el área del triángulo o conocer el tipo de triángulo
        \n Ingrese 1 para conocer el área de un triángulo o 2 para conocer el tipo de triángulo.    
        """))
        try:
            if opt == 1:
                try:
                    b = float(input("ingresa la base del triángulo:  "))
                    h = float(input("ingresa la altura del triángulo:  "))
                    print(f"El área del triángulo es {area(b,h)}")
                    break
                except ValueError:
                    print("Por favor introduce solo valores numericos")
            elif opt == 2:
                try:
                    l1 = float(input("ingresa la medida del lado 1: "))
                    l2 = float(input("ingresa la medida del lado 2: "))
                    l3 = float(input("ingresa la medida del lado 3: "))
                    tipo_triangulo(l1,l2,l3)
                    break
                except ValueError:
                    print("Por favor introduce solo valores numericos")
        except ValueError:
                print("Por favor introduce la opción 1 o 2")
        

if __name__ == '__main__':
    main()