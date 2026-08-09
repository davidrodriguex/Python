from random import choice

def valida_num(msg):
    while True:
        try:
            valor = int(input(msg))
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

classificacao = ["Fraca", "Média", "Forte"]
senha = ""
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

tamanhoSenha = valida_num("Escolha o tamanho da senha (mínimo 4 caracteres): ")

while len(senha) < tamanhoSenha:
    senha += choice(caracteres)
    
print(f"\nSenha gerada: {senha}")

if len(senha) < 6:
    print(f"Classificação da senha: {classificacao[0]}")
elif len(senha) < 8:
    print(f"Classificação da senha: {classificacao[1]}")
else:
    print(f"Classificação da senha: {classificacao[2]}")