print("--- Aula Pratica Sobre Exceções ---")

while True:
    try:
        num1 = float(input("Digite seu primeiro número: "))
        num2 = float(input("Digite seu segundo número: "))
        
        resultado = num1 / 0
        print(f"Resultado: {resultado}")
        
    except ValueError:
        print("Erro: Por favor, digite apenas números!")
        
    except ZeroDivisionError:
        print("Erro: Não e possivel dividir esse numero por zero!")
        
    finally:
        print("Fim do programa!")
    
    opcao = input("\nQuer fazer outra conta? (s/n): ")
    
    if opcao.lower() != 's':
        print("Até logo!")
        break
