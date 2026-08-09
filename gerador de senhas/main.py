from random import randint, choice

def validaNum(tamTexto):
    while True:
        try:
            valor = int(input(tamTexto))
        except ValueError:
            print("ERRO! Digite um número inteiro válido.")
            continue
        else:
            if valor < 4:
                print("ERRO! O tamanho da senha deve ser no mínimo 4 caracteres.")
                continue
            else:
                return valor

print("-" * 30)
print("Gerador de Senhas".center(30))
print("-" * 30)
print()

listaSorteio = []
listaLetrasMaiusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                                    "U", "V", "W", "X", "Y", "Z"]
listaLetrasMinusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                                    "t", "u", "v", "w", "x", "y", "z"]
listaNumeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

tamanhoSenha = validaNum("Escolha o tamanho da senha (mínimo 4 caracteres): ")
sorteio = randint(1, tamanhoSenha)

while len(listaSorteio) < tamanhoSenha:
    if sorteio == 1:
        listaSorteio.append(choice(listaLetrasMaiusculas))
    elif sorteio == 2:
        listaSorteio.append(choice(listaLetrasMinusculas))
    elif sorteio == 3:
        listaSorteio.append(choice(listaNumeros))
    else:
        continue
    sorteio = randint(1, tamanhoSenha)

senha = "".join(listaSorteio)
print(f"\nSenha gerada: {senha}")