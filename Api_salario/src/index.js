const express = require('express');
const server = express();
const PORT = 3000;

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

const dicionario = Dict_porc(`Despesas=60,Investimento=30.0,Fundo Emergencial=5.0,Pode gastar=5.0`)
const calculo = Calc(dicionario,2650)

server.get('/',(req,res) => {
    return res.json(calculo)
})

server.post('/salario/:id', (req, res) => {
    const id = req.params.id; // Access the dynamic segment
    const calculo = Calc(dicionario,id)
    res.send(calculo);
})

server.post('/atualizarDict/:desp/:inv/:fundoEmergencial/:podeGastar/:id', (req, res) => {
    const despesas = req.params.desp
    const investimento = req.params.inv
    const fundoEmergencial = req.params.fundoEmergencial
    const podeGastar = req.params.podeGastar
    const salario = req.params.id

    const dicionario = Dict_porc(`Despesas=${despesas},Investimento=${investimento},Fundo Emergencial=${fundoEmergencial},Pode gastar=${podeGastar}`)
    const calculo = Calc(dicionario,salario)

    res.send(calculo)
})

server.listen(3000, () => {
    console.log('Servidor está funcionando...')
    })
