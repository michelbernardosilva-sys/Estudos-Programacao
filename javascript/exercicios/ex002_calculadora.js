// Exercício 002 - Calculadora Simples
// Objetivo: Praticar operadores e funções

function calculadora(a, b) {
    console.log(`Soma:          ${a + b}`);
    console.log(`Subtração:     ${a - b}`);
    console.log(`Multiplicação: ${a * b}`);
    console.log(`Divisão:       ${(a / b).toFixed(2)}`);
}

calculadora(10, 3);
