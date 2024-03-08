import express from "express";
import bodyParser from "body-parser";
import validarParametros from "../code/validarParam.js"

const app = express();

app.get('/', (req, res)=>{
    res.status(200).send('API Rodando, por favor, coloque a rota "/gerar" para testar a aplicação.');
});

app.get('/gerar', bodyParser.json(), (req, res)=>{
    const quantidade = req.body.quantidade;
    const numero = req.body.numero;
    const maiusculo = req.body.maiusculo;
    const minusculo =  req.body.minusculo;
    const simbolo = req.body.simbolo;

    // Começa a chamada dos arquivos do gerador de senha, que estão todos na pasta "code"
    let senha = validarParametros(quantidade, numero, maiusculo, minusculo, simbolo)
    res.status(200).send(senha);
})

export default app;