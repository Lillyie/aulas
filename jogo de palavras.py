#jogo da Forca
import random

palavras_profissoes = [
    "medico", "engenheiro", "professor", "programador", "advogado",
    "designer", "arquiteto", "enfermeiro", "contador", "jornalista"
]

palavras_desenhos = [
    "pokemon", "naruto", "simpsons", "avatar", "ben10",
    "gravityfalls", "gumball", "rickandmorty", "stevenuniverse", "ducktales"
]

palavras_animais = [
    "cachorro", "gato", "elefante", "leao", "tigre",
    "girafa", "zebra", "golfinho", "tubarao", "urso"
]

palavras_jogos = [
    "minecraft", "fortnite", "zelda", "mario", "sonic",
    "valorant", "overwatch", "amongus", "roblox", "tetris",
    "pokemon", "doom", "skyrim", "halo", "portal"
]

palavras_filmes_series = [
    "matrix", "inception", "avatar", "titanic", "gladiador",
    "interestelar", "harrypotter", "senhordosaneis", "starwars", "jurassicpark",
    "breakingbad", "dark", "lost", "friends"
]



print("Selecione o modo de jogo")
print("-" * 30)
print("1 - profissões")
print("2 - desenhos")
print("3 - animais")
print("4 - jogos")
print("5 - filmes/series")
print("-" * 30)
modo = input("")

if modo == "1":
    word_list = palavras_profissoes
elif modo == "2":
    word_list = palavras_desenhos
elif modo == "3":
    word_list = palavras_animais
elif modo == "4":
    word_list = palavras_jogos
elif modo == "5":
    word_list = palavras_filmes_series
else:
    print("modo inválido!")
    exit()



select_word = random.choice(word_list)

error = 0
letras_acertadas = ""

while True:
    var_try = input("digite uma letra: ").lower().strip()
    if len(var_try) > 1:
        if var_try == select_word:
            print("você acertou!")
            break
        elif var_try != select_word:
            print("você errou o chute!")
        else:
            print("por favor digite apenas 1 letra.")
        continue

    if var_try in select_word:
        if var_try not in letras_acertadas:
            letras_acertadas += var_try
            print("você acertou!")
        else:
            print("você ja tentou esta letra. Tente outra.")
    else:
        error += 1
        print(f"Você errou pela {error}º vez!")

    progresso = ''
    for letra in select_word:
        if letra in letras_acertadas:
            progresso += letra
        else:
            progresso += "_"

    print("palavra: ", progresso)
    print("-"*30)

    if "_" not in progresso:
        if error >= 0:
            print(f"Você ganhou! \nVocê errou apenas{error} vezes!")
        elif error == 0:
            print("Você ganhou e nao errou NENHUMA VEZ!")
        
        break