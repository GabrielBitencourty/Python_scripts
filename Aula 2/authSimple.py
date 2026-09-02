def validar_senha(senha):
    erros = []
    
    if len(senha) < 8:
        erros.append("- Ter pelo menos 8 caracteres")
    tem_letra = any(c.isalpha() for c in senha)
    if not tem_letra:
        erros.append("- Ter pelo menos uma letra")
    tem_numero = any(c.isdigit() for c in senha)
    if not tem_numero:
        erros.append("- Ter pelo menos um número")
    tem_especial = any(not c.isalnum() for c in senha)
    if not tem_especial:
        erros.append("- Ter pelo menos um caractere especial")
    if len(erros) == 0:
        return "Forte", erros
    else:
        return "Fraca", erros

senha_teste = input("Crie uma senha de acesso: ")
status, pendencias = validar_senha(senha_teste)

print(f"\nResultado da Avaliação: Senha {status}")
if status == "Fraca":
    print("Sua senha precisa melhorar nos seguintes pontos:")
    for erro in pendencias:
        print(erro)
