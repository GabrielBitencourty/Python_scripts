produtos = []

for i in range(1, 6):
    print(f"\n--- Cadastro do Produto {i} ---")
    nome = input("Nome do produto: ")
    preco = float(input("Preço unitário (R$): "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "valor_estoque": preco * quantidade
    }
    produtos.append(produto)

produto_mais_caro = produtos[0]
produto_mais_barato = produtos[0]
valor_total_global = 0

print("\n--- Valor em Estoque por Produto ---")
for prod in produtos:
    print(f"Produto: {prod['nome']} | Valor em Estoque: R$ {prod['valor_estoque']:.2f}")
    valor_total_global += prod['valor_estoque']
    if prod['preco'] > produto_mais_caro['preco']:
        produto_mais_caro = prod
    if prod['preco'] < produto_mais_barato['preco']:
        produto_mais_barato = prod

print("\n--- Relatório Financeiro Geral ---")
print(f"Produto mais caro: {produto_mais_caro['nome']} (R$ {produto_mais_caro['preco']:.2f})")
print(f"Produto mais barato: {produto_mais_barato['nome']} (R$ {produto_mais_barato['preco']:.2f})")
print(f"Valor total de todo o estoque da empresa: R$ {valor_total_global:.2f}")
