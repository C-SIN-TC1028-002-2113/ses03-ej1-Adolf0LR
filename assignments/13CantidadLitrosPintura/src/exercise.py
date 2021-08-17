import math
def main():
    #escribe tu código abajo de esta línea
    m = float(input("Area a pintar en metros: "))
    ren = float(input("Rendimiento (m2/l): "))
    litros = m/ren
    print("Litros a comprar:",math.ceil(litros)) 

if __name__ == '__main__':
    main()
