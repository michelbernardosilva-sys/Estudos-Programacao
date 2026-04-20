// Exercício 002 - Calculadora Simples
// Objetivo: Praticar operadores e scanf
#include <stdio.h>

int main() {
    float a, b;

    printf("Digite o primeiro número: ");
    scanf("%f", &a);
    printf("Digite o segundo número: ");
    scanf("%f", &b);

    printf("Soma:          %.2f\n", a + b);
    printf("Subtração:     %.2f\n", a - b);
    printf("Multiplicação: %.2f\n", a * b);
    printf("Divisão:       %.2f\n", a / b);

    return 0;
}
