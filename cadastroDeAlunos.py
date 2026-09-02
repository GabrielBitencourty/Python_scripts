turma = [
    {"nome": "Carlos", "idade": 16},
    {"nome": "Mariana", "idade": 19},
    {"nome": "Pedro", "idade": 15},
    {"nome": "Juliana", "idade": 22}
]


menores_de_idade = 0
maiores_de_idade = 0

print("--- Relatório de Cadastro de Alunos ---")

for aluno in turma:
    nome = aluno["nome"]
    idade = aluno["idade"]
    
    if idade >= 18:
        classificacao = "Maior de idade"
        maiores_de_idade += 1
    else:
        classificacao = "Menor de idade"
        menores_de_idade += 1
        
    print(f"Nome: {nome:<10} | Idade: {idade} anos | Status: {classificacao}")


print("\n--- Estatísticas Finais ---")
print(f"Total de alunos menores de 18 anos: {menores_de_idade}")
print(f"Total de alunos maiores de 18 anos: {maiores_de_idade}")
