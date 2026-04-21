# 🐍 Python

| Exercicio  04       | Conteúdo                          |
Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema deve calcular a alíquota de imposto de renda (IR) que deve ser aplicada sobre aquele resgate, levando em consideração o número de dias que o valor permaneceu aplicado, de acordo com a tabela abaixo:

 

Até 180 dias = alíquota de 22,5% de IR.

De 181 a 360 dias = alíquota de 20% de IR.

De 361 a 720 dias = alíquota de 17,5% de IR.

Acima de 720 dias = alíquota de 15% de IR.

 

É o que acontece, por exemplo, com o Certificado de Depósito Bancário (CDB), uma aplicação de renda fixa comumente oferecida pelas Fintechs. Outros investimentos em renda fixa, como LCI e LCA, respectivamente, Letra de Crédito Imobiliário e Letra de Crédito do Agronegócio são isentos de imposto de renda. Escreva um programa que receba o tipo de investimento do qual se deseja realizar um resgate (1 para CDB, 2 para LCI e 3 para LCA), o valor a ser resgatado e o número de dias que esse valor permaneceu investido e, se for o caso, calcule o valor referente ao imposto de renda.

Atenção! O programa deve consistir se o investimento fornecido é válido, ou seja, 1, 2 o 3.

Modelo de saída:
    MENU DE INVESTIMENTO   

Escolha o tipo de investimento:
1- CDB
2- LCI
3- LCA

Digite o tipo de investimento (1, 2 ou 3): 1
Digite o valor a ser resgatado: 10
Digite o número de dias que o valor permaneceu investido: 10
O valor do imposto de renda a ser pago é: R$ 2.25