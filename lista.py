adicionar = float(input("Qual o valor/nota à ser adicionado?: "))
 
notas = [7.0, 1.5, 10.0, 8.5, 3.0]
notas.append(adicionar)





# contador = 0
# limite = len(notas) - 1

# while contador <= limite:
#     print (f"sua nota é nota é: {notas[contador]}")
#     contador += 1

for x in notas:
    print(f"Sua nota é: {x}")