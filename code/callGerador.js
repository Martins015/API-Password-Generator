import shell from 'shelljs';
shell.cd('code'); 

//Realiza a chamada do gerador com um comando shell
export default function callPython(quantidade, numero, maiusculo, minusculo, simbolo){
    return shell.exec(`gerador.py ${quantidade} ${numero} ${maiusculo} ${minusculo} ${simbolo}`).toString();
};
