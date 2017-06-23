
# Exercícios

## Fluxo simples

### 1. Centímetros e metros

Escreva um programa que pergunta a altura da pessoa em centímetros e exiba a altura em metros, neste formato:

`Sua altura é 1.78m.`

### 2. IMC - Índice de Massa Corporal

Escreva um programa que pergunta a altura da pessoa em centímetros, depois pede seu peso em Kg. Com esses dados, o programa deve computar e exibir o IMC (Índice de Massa Corporal) da pessoa.

Dado o peso `P` em Kg e altura em metros `A`, a fórmula do o IMC é: `P / A²`,

### 3. Minutos e horas

Escreva um programa que solicita a duração de um filme em minutos, e exibe a duração em horas e minutos, neste formato:

`O filme dura 2h15.`

Para calcular horas cheias a partir de minutos, use a fórmula:

`horas = minutos // 60`

Considerando 135 minutos, o resultado da operação acima é 2, porque o operador `//` devolve a divisão como um número inteiro.

Para obter a "sobra" de minutos (o resto da divisão por minutos), use a fórmula:

`horas = minutos % 60`

Considerando 135 minutos, o resultado da operação acima é 15.


### 4. Pés e polegadas

Escreva um programa que pergunta a altura da pessoa em centímetros e exiba a altura em metros, neste formato:

`Sua altura é 5'10"`

Onde `5'` significa "5 pés" e `10"` significa "10 polegadas".

Para fazer o cálculo, considere que `1" = 2.54cm` e que `1' = 12"`.

**Dica**: use os operadores mostrados no exercício **Minutos e horas**.
