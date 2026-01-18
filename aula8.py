list_compras = []

print("\tLISTA DE COMPRAS")
print("-" *40)
print("L - Listar \nI - Inserir \nR - Remover")
print("-" *40)
i = 1

while True:
    print("O que você deseja fazer?")
    cmd = input("").strip().capitalize()
    print("-" *40)
    
    if cmd.startswith("I"):
        inserir = input("Qual item você quer inserir na lista? ")
        list_compras.append(inserir)
        
        for itens in list_compras:
            print(i, list_compras)
    
            i+=1
        continue
    i = 0
    if cmd.startswith("L"):
        print(list_compras)
        
        if len(list_compras) == 0:
            print("Nada na lista")
        continue

    print("aa")
