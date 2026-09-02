def analisar_sequencia(numeros):
    if not numeros:
        return 0, 0, 0, 0, 0

    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    
    contagem_pares = 0
    for num in numeros:
        if num % 2 == 0:
            contagem_pares += 1
            
    return soma, media, contagem_pares, maior, menor

dados_originais = [12, 5, 8, 21, 14, 7]

s, m, pares, maximo, minimo = analisar_sequencia(dados_originais)

print(f"Soma total: {s}")
print(f"Média aritmética: {m:.2f}")
print(f"Quantidade de números pares: {pares}")
print(f"Maior valor: {maximo}")
print(f"Menor valor: {minimo}")
