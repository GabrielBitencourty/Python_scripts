# 🎓 Atividade Prática: Análise de Códigos em Python

Este repositório foi criado para armazenar e organizar os scripts desenvolvidos durante as aulas de Paradigmas de Llinguagen de programação em python da minha faculdade. O objetivo principal desta atividade é analisar a lógica de programação, identificar os elementos fundamentais do Python e propor melhorias profissionais em cenários reais.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Ambiente:** Terminal / IDE (VS Code, PyCharm, etc.)
* **Conceitos Aplicados:** Funções, Estruturas de Decisão (`if/elif/else`), Estruturas de Repetição (`for/while`), Variáveis, Tipos de Dados e Estruturas Compostas.

---

## 📂 Scripts Desenvolvidos

### 📊 1. Análise de Desempenho Acadêmico
* **Descrição:** Recebe três notas de um estudante, realiza o cálculo da média aritmética e gera o status final do aluno.
* **Classificações:** Aprovado ($\geq 7.0$), Recuperação (entre $5.0$ e $6.9$) ou Reprovado ($< 5.0$).
* **Identificação de Elementos:**
  * **Variáveis/Tipos:** `nota1` (float), `media` (float), `situacao` (string).
  * **Estrutura de Decisão:** `if/elif/else`.
  * **Melhoria Implementada:** Validação para impedir a entrada de notas negativas ou maiores que 10.

### 🔢 2. Análise de Sequência Numérica
* **Descrição:** Processa um conjunto de números inteiros para extrair dados estatísticos fundamentais de produção ou amostragem.
* **Métricas Geradas:** Soma total, média decimal, contagem de números pares, maior e menor valor encontrado.
* **Identificação de Elementos:**
  * **Variáveis/Tipos:** `numeros` (list), `contagem_pares` (int).
  * **Estrutura de Repetição:** Laço `for` para varredura da lista.
  * **Melhoria Implementada:** Tratamento de erro caso a lista seja enviada vazia.

### 💰 3. Sistema de Descontos Profissional
* **Descrição:** Simula o fechamento de um caixa ou sistema de vendas, aplicando descontos percentuais customizados a partir de funções modulares.
* **Destaque:** Uso estrito de **funções com passagem de parâmetros e retorno de valores**.
* **Identificação de Elementos:**
  * **Variáveis/Tipos:** `valor_bruto` (float), `taxa_desconto` (float).
  * **Melhoria Implementada:** Automação de faixas de descontos com base no valor total comprado.

### 👥 4. Cadastro e Classificação de Alunos
* **Descrição:** Gerencia o fluxo de cadastro de uma turma utilizando coleções de dados, realizando a contagem automatizada de faixas etárias.
* **Identificação de Elementos:**
  * **Estruturas Compostas:** Dicionários (`dict`) aninhados dentro de uma Lista (`list`).
  * **Contadores:** Variáveis acumuladoras simples (`+= 1`).
  * **Melhoria Implementada:** Integração com o Script 1 para guardar também o histórico de notas dentro do dicionário de cada estudante.

---

## 📈 Como Executar os Projetos

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com
   ```
3. Acesse a pasta do projeto e execute qualquer um dos scripts:
   ```bash
   python nome_do_script.py
   ```

---
💡 *Projeto desenvolvido como parte do meu aprendizado acadêmico em Engenharia/Ciência da Computação/Análise e Desenvolvimento de Sistemas.*
