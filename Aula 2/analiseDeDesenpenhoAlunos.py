nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
faltas = int(input("Digite a quantidade de faltas: "))

media = (nota1 + nota2 + nota3) / 3

if faltas > 10:
    situacao = "Reprovado por falta"
elif media >= 7:
    situacao = "Aprovado"
elif 5 <= media < 7:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n--- Resultado Final ---")
print(f"Aluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
