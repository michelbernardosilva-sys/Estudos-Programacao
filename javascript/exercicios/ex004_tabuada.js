// Exercício 004 - Tabuada
// Objetivo: Praticar loops

function tabuada(numero) {
    console.log(`\nTabuada do ${numero}:`);
    for (let i = 1; i <= 10; i++) {
        console.log(`${numero} x ${i} = ${numero * i}`);
    }
}

tabuada(7);
