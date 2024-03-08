import callPython from '../code/callGerador.js';

// Função criada para verificar se faltou algum parâmetro na chamada do gerador.
export default function validarParametros(quantidade, numero, maiusculo, minusculo, simbolo){
    let resultado
    switch(undefined){
        case quantidade:
            resultado = 'Quantidade de parâmetros insuficiente';
            break;
        case numero:
            resultado = 'Quantidade de parâmetros insuficiente';
            break;
        case maiusculo:
            resultado = 'Quantidade de parâmetros insuficiente';
            break; 
        case minusculo:
            resultado = 'Quantidade de parâmetros insuficiente';
            break;
        case simbolo:
            resultado= 'Quantidade de parâmetros insuficiente';
            break;
        default:
            resultado = callPython(quantidade, numero, maiusculo, minusculo, simbolo);
    }
    return resultado;   
};