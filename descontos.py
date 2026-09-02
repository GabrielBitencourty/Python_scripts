def calcular_preco_final(valor_total, porcentagem_desconto):
    valor_do_desconto = valor_total * (porcentagem_desconto / 100)
    preco_final = valor_total - valor_do_desconto
    return preco_final

valor_compra = 250.00
desconto = 15.0 

resultado_final = calcular_preco_final(valor_compra, desconto)


print(f"Valor original da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor final a pagar: R$ {resultado_final:.2f}")
