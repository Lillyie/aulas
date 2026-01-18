# exercício 

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

print('-'*30)
if nome and idade:
    print(f'seu nome é: {nome}')
    print(f'seu nome invertido é: {nome[::-1]}')
    print('-'*30)
    if ' ' in nome:
        print(f'seu nome contém espaços')
    else:
        print(f'seu nome não contém espaços')
    print('-'*30)
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é: "{nome[0]}"')
    print(f'a última letra do seu nome é "{nome[-1]}"')
else:
    print("por favor digite em todos os campos")
print('-'*30)
print("fim do código")
print('-'*30)


#tuff

#correção do código pelo chatgpt
'''
        # .strip() serve pra remover os espaços antes e depois da palavra, por exempo "  mateus  ", vai printar "mateus"
nome = input("Digite seu nome: ").strip()
idade = input("Digite sua idade: ").strip()

print("-" * 30)

if not nome or not idade:
    print("Por favor, preencha todos os campos.")
else:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")

    print("-" * 30)
        
        # o IF desta linha vai ler o que está atras dele, tipo um "fale isso, *caso* aconteça aquilo. 
    print("Seu nome contém espaços." if " " in nome else "Seu nome não contém espaços.")

    
    print("-" * 30)

    print(f"Seu nome tem {len(nome)} letras.")
    print(f'A primeira letra do seu nome é: "{nome[0]}"')
    print(f'A última letra do seu nome é: "{nome[-1]}"')

print("-" * 30)
print("Fim do código")
print("-" * 30)
'''