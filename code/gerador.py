import random
import sys 

# Criando variáveis com os parâmetros passados na chamada do gerador
paramQuantidade = int(sys.argv[1])
paramNumero = str(sys.argv[2]).lower()
paramMaiusculo = str(sys.argv[3]).lower()
paramMinusculo = str(sys.argv[4]).lower()
paramSimbolo = str(sys.argv[5]).lower()

# Criando lista com as letras maiusculas, minusculas e simbolos
maiusculos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
minusculos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
simbolos = ['@', '#', '$', '%', '*', '!']

# Criando funções para pegar os componentes das listas
def fnGetNumero():
    return str(random.randint(0, 9))

def fnGetMaiusculos(): 
    return maiusculos[random.randint(0, 25)]

def fnGetMinusculos(): 
    return minusculos[random.randint(0, 25)]

def fnGetSimbolos(): 
    return simbolos[random.randint(0, 5)]


def fnGerador(quantidade, numero, maiusculo, minusculo, simbolo): 
    contador = 0 
    senha = ''
    funcoes = []

    # Filtrando os parâmetros para colocar na senha
    if(quantidade < 1 or (numero == 'n' and maiusculo == 'n' and minusculo == 'n' and simbolo == 'n')):
        return "Quantidade de parametros insuficiente. Digite ao menos 1 atributo como verdadeiro (S) e um numero maior do que 0."
    else: 
        if(numero == 's'): 
            funcoes = [fnGetNumero]
        if(maiusculo == 's'): 
            funcoes += [fnGetMaiusculos]
        if(minusculo == 's'): 
            funcoes += [fnGetMinusculos]
        if(simbolo == 's'):  
            funcoes += [fnGetSimbolos]

        while(contador < quantidade):
            senha += funcoes[random.randint(0, len(funcoes) - 1)]()
            contador += 1
        return senha 

print(fnGerador(paramQuantidade, paramNumero, paramMaiusculo, paramMinusculo, paramSimbolo))

sys.stdout.flush()