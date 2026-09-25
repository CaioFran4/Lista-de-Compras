# FORMAS OBRIGATÓRIAS:
#   1 - Círculo
#   2 - Trângulo
#   3 - Quadrado
#   4 - Retângulo
#   5 - Paralelogramo
#   6 - Lozango
#   7 - Trapézio

def circle():
    diametro = float(input("Qual o diametro do Circulo?: "))
    raio = diametro / 2
    print(f"O raio do Circulo é igual a {raio}")

def trian():
    base = float(input("Qual a Base do Triângulo?: "))
    altura = float(input("Qual a Altura do Triângulo?: "))
    area = base * altura / 2
    print(f"A Área do Triângulo é {area}")
    
    
def quadra():
    lado1 = float(input("Qual a medida do lado1?: "))
    lado2 = float(input("Qual a medida do lado2?: "))
    area = lado1 * lado2
    print(f"A Área do Quadrado é {area}")


def reta():
    base = float(input("Qual a base do Retângulo?: "))
    altura = float(input("Qual a Altura do Retângulo?: "))
    area = base * altura
    print(f"A Área do Retângulo é {area}")
    
def parale():
    base = float(input("Qual a base do Paralelogramo?: "))
    altura = float(input("Qual a Altura do Paralelogramo?: "))
    area = base * altura
    print(f"A Área do Paralelogramo é {area}")

def loza():
    diagonal_maior = float(input("Qual é o diagonal maior?:"))
    diagonal_menor = float(input("Qual é o diagonal menor?: "))
    area = diagonal_maior * diagonal_menor /2
    print(f"A Área do Lozango é {area}")
    
def trape():
    base_maior = float(input("Qual o valor da maior base?: "))
    base_menor = float(input("Qual o valor menor base?: "))
    altura = float(input("Qual o valor da altura?: "))
    area = base_maior + base_menor * altura /2
    print(f"A Área do Trapézio é {area}")















while True:
    print("1 - Círculo")
    print("2 - Trângulo")
    print("3 - Quadrado")
    print("4 - Retângulo")
    print("5 - Paralelogramo")
    print("6 - Lozango")
    print("7 - Trapézio")
    print("0 - Desligar Sístema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        circle()

    elif opcao == "2":
        trian()

    elif opcao == "3":
        quadra()

    elif opcao == "4":
        reta()

    elif opcao == "5":
        parale()

    elif opcao == "6":
        loza()

    elif opcao == "7":
        trape()

    elif opcao == "0":
        print ("Desligando sistema.")
        break


