print("-" * 30)
print("Gerador de Senhas".center(30))
print("-" * 30)
print()
listaSorteio = {
    'letrasMin': "abcdefghijklmnopqrstuvwxyz",
    'letrasMai': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    'numeros': "0123456789",
    'simbolos': "!@#$%^&*()-+"
}
tamanhoSenha = int(input("Escolha o tamanho da senha (mínimo 4 caracteres): "))