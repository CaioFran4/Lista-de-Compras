lista_completa = []
def list():
        print(lista_completa)

def add():
    adicionar = input("qual item você gostaria de adicionar á lista?: ")
    lista_completa.append (adicionar)

def exc():
    excluir = input("qual item você gostaria de excluir da lista?: ")
    lista_completa.remove (excluir)

def mod():
     modificar = input("Qual item você gostaria de modificar?: ")
     lista_completa.index (modificar)
     lista_completa.remove (modificar)
     modificar_item = input("Qual item sera adicionado no lugar?: ")
     lista_completa.append (modificar_item)


while True:
    print("- Lista de Compras -")
    print("1 - Mostrar Lista")
    print("2 - Cadastrar item á Lista")
    print("3 - Excluir item da Lista")
    print("4 - Modificar item da Lista")
    print("0 - Sair")

    opcao = input("Qual ação você deseja fazer?: ")
    
    if opcao == "1":
        list()

    elif opcao == "2":
        add()
    
    elif opcao == "3":
        exc()
    
    elif opcao == "4":
        mod()

    elif opcao == "0":
         print("Saindo do Sistema")
         break


