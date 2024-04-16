familia = ["Higor", "Larissa", "Lucas", "Gabriel", "Arthur"]
#             0         1         2         3         4
#            -5        -4        -3        -2        -1

#print(familia)
#print(familia[3]) #retorna um indice
#print(familia[-1]) #retorna um indice de traz pra frente
#print(familia[2:]) #retorna a partir do indice 2
#print(familia[2:4]) #retorna a partir do indice 2 até o 4, excluindo o 4

#print(familia)
familia[3] = "Higor"
#print(familia)

familia.extend(["Isaac","Matheus"])
#print(familia) 

familia.append("Zed cachorro") #insere no final da lista
familia.insert(1,"Zed cachorro") #insere na colocação desejada
familia.pop() #remove o ultimo da lista
familia.remove("Zed cachorro") #remove o nome especifico

#print(familia)

familia.clear() #remove todos os itens da lista

#print(familia.index("Higor")) #mostra a posição do item na lista
#print(familia.count("Higor")) #conta quantos itens tem na lista

#print(familia)

idade_familia = [20,3,20,22,21,14,19,20]

#print(idade_familia)

idade_familia.sort()
#print(idade_familia)
familia.sort() #ordena a lista
#print(idade_familia)
#print(familia)

idade_familia.reverse() #inverte a ordem da lista

#print(idade_familia)

familia2= familia #copia de referencia
#print(familia2)
familia.remove("Higor")
#print(familia2)

familia2= familia.copy()

coordenadas = (-49,-36) #tuples = imutavel
coordenadas.pop()
#print(coordenadas)
#print(coordenadas[0])
#print(coordenadas.count(-49))