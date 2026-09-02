PRECO_KWH = 1.15

consumos = []
valores_pago = []

for i in range(1, 7):
    valor = float(input(f"Digite o consumo do mês {i} (kWh): "))
    consumos.append(valor)
    
    valor_reais = valor * PRECO_KWH
    valores_pago.append(valor_reais)

media_consumo = sum(consumos) / len(consumos)
maior_consumo = max(consumos)
menor_consumo = min(consumos)
posicao_maior = consumos.index(maior_consumo) + 1

total_pago = sum(valores_pago)
custo_medio = media_consumo * PRECO_KWH

meses_acima_media = 0
for valor in consumos:
    if valor > media_consumo:
        meses_acima_media += 1

print("\n" + "="*38)
print("--- RELATÓRIO DE CONSUMO ELÉTRICO ---")
print("="*38)
print(f"Consumo Médio:          {media_consumo:.2f} kWh (Est. R$ {custo_medio:.2f})")
print(f"Maior Consumo:          {maior_consumo:.2f} kWh (Mês {posicao_maior})")
print(f"Menor Consumo:          {menor_consumo:.2f} kWh")
print(f"Meses Acima da Média:   {meses_acima_media}")
print("-"*38)
print(f"VALOR TOTAL ESTIMADO:   R$ {total_pago:.2f}")
print("="*38)
print(f"Nota: Baseado na tarifa média estimada de R$ {PRECO_KWH:.2f}/kWh de MG.")
