notas = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 10.0, 3.5, 8.5, 7.0]

media_turma = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)

aprovados = 0
recuperacao = 0
reprovados = 0

for nota in notas:
    if nota >= 7.0:
        aprovados += 1
    elif 5.0 <= nota < 7.0:
        recuperacao += 1
    else:
        reprovados += 1

print("========================================")
print("       RELATÓRIO ACADÊMICO FINAL       ")
print("========================================")
print(f"Média Geral da Turma : {media_turma:.2f}")
print(f"Maior Nota Registrada: {maior_nota:.1f}")
print(f"Menor Nota Registrada: {menor_nota:.1f}")
print("----------------------------------------")
print(f"Alunos Aprovados     : {aprovados}")
print(f"Alunos em Recuperação: {recuperacao}")
print(f"Alunos Reprovados    : {reprovados}")
print("========================================")
