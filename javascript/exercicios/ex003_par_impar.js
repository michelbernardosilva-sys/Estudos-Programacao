// Exercício 003 - Par ou Ímpar
// Objetivo: Praticar condicionais e operador módulo

function parOuImpar(numero) {
    if (numero % 2 === 0) {
        return `${numero} é PAR`;
    } else {
        return `${numero} é ÍMPAR`;
    }
}

console.log(parOuImpar(4));
console.log(parOuImpar(7));
