from random import choice

def interface():
    print("-" * 30)
    print("Gerador de Senhas".center(30))
    print("-" * 30)
    print()

def menu(opcoes):
    for opcao in opcoes:
        print(opcao)
    print()
    while True:
        valor = valida_num("Escolha uma opção: ")
        if 1 <= valor <= len(opcoes):
            return valor
        else:
            print("ERRO! Digite uma opção válida.")

def valida_num(msg):
    while True:
        try:
            valor = int(input(msg))
        except ValueError:
            print("ERRO! Digite um número inteiro válido.")
            continue
        else:
            return valor

# Código Principal

interface()
opcao_menu = menu(["1 - Apenas letras", "2 - Letras e números", "3 - Letras, números e símbolos"])

classificacao = ["Fraca", "Média", "Forte"]
senha = ""
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

while True:
    tamanhoSenha = valida_num("Escolha o tamanho da senha (mínimo 4 caracteres): ")
    if tamanhoSenha < 4:
        print("ERRO! O tamanho da senha deve ser no mínimo 4 caracteres.")
    else: break

while len(senha) < tamanhoSenha:
    senha += choice(caracteres)
    
print(f"\nSenha gerada: {senha}")

if len(senha) < 6:
    print(f"Classificação da senha: {classificacao[0]}")
elif len(senha) < 8:
    print(f"Classificação da senha: {classificacao[1]}")
else:
    print(f"Classificação da senha: {classificacao[2]}")