const express = require('express');
const server = express();

function Dict_porc(args) {
    let dicionario = {}
    const listArgs = args.split(',') 
    for (let i = 0; i < listArgs.length; i++) {
        const elemento = listArgs[i].split('=')
        for (let j = 0; j < elemento.length; j++) {
            dicionario[elemento[j]] = elemento[j + 1]
            break
        }
    }

    return dicionario
}

function Calc(dicionario,salario) {
    let dict = {};
    const tamanho = Object.keys(dicionario).length;
    for (let i = 0; i < tamanho; i++) {
        const key = Object.keys(dicionario)[i];
        const resultado = (salario * dicionario[key] / 100).toFixed(2)
        dict[key] = resultado
    }
    return dict
}

const dicionario = Dict_porc('Despesas=60.0,Investimento=30.0,Fundo Emergencial=5.0,Pode gastar=5.0')
const calculo = Calc(dicionario,2650)

server.get('/',(req,res) => {
    return res.json(calculo)
})

server.listen(3000, () => {
    console.log('Servidor está funcionando...')
    })