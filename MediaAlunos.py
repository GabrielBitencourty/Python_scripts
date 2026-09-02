def analisar_desempenho(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    
    if media >= 7.0:
        situacao = "Aprovado"
    elif 5.0 <= media < 7.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
        
    return media, situacao

nome_aluno = "Ana Silva"
n1, n2, n3 = 8.5, 6.0, 7.5

media_final, status = analisar_desempenho(n1, n2, n3)

print(f"Aluno(a): {nome_aluno}")
print(f"Média Final: {media_final:.1f}")
print(f"Situação: {status}")
