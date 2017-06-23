# Exercícios

## Condicionais com `if`

### 1. Filhotes de cachorro

Escreva um programa que pede a idade de um cachorro em meses e informa se ele é considerado um filhote ou não, considerando que filhotes têm até 11 meses de idade.

Por exemplo:

```
Digite a idade do cachorro em meses: 15
Este cachorro não é mais um filhote.
```

### 2. Fases da vida do cachorro

Escreva um programa que pede a idade de um cachorro em anos e informa o estágio seu estágio de vida, conforme os anos de vida informados nesta tabela:

```
|            menos de 1 ano | filhote     |
| de 1 a 3 anos incompletos | adolescente |
|            3 ou mais anos | adulto      |
```

### 3. Excesso de velocidade

Faça um programa que aplica multas por excesso de velocidade. O programa pergunta a velocidade do veículo e, caso ela seja até 80km/h, informa `Velocidade permitida`.

Se a velocidade for maior que 80km/h, o programa calcula uma multa no valor de R$ 200 + R$ 5 por cada km/h acima de 80.

Por exemplo, se a velocidade for 87km/h, a multa será de R$ 235 (200 + 7 * 5).


### 4. Excesso de velocidade (regra no Brasil)

No Brasil, em 2017, a regra para multas de excesso de velocidades é:

- Exceder velocidade em até 20% (infração média): R$85,00 e 4 pontos na carteira.
- Exceder velocidade de 20 até 50% (infração grave): R$127,00 e 5 pontos na carteira.
- Exceder velocidade acima de 50% (infração gravíssima): R$574,00, 7 pontos, apreensão da carteira, suspensão do direito de dirigir.

Escreva um programa que solicita qual é a velocidade permitida e qual é a velocidade do veículo e informa o valor da multa e outras punições se for o caso.

Exemplo:

```
Informe a velocidade permitida: 100
Informe a velocidade do veículo: 130
***RESULTADO***
Infração grave: multa de R$ 127 e 5 pontos na carteira.
```
