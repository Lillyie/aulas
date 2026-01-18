first  = input("digite um valor: ")
secnd = input("digite um outro valor:")


if first == secnd:
    print("são o mesmo valor!")    
elif first > secnd:
    print(f'{first} é maior que {secnd}!')
elif secnd > first:
    print(f'{first} é menor que {secnd}!')
else:
    print ("vixi")
