# Api Password Generate 

## Descrição 
- A Api Password Generate é uma ferramenta de API que gera senhas aleatórias baseadas em 4 parâmetros
fornecidos no corpo da requisição GET com JSON.

## Funcionalidades
- Gerar senhas aleatórias com um comprimento configurável;
- Permite especificar se a senha deve conter letras maiúsculas, minúsculas, números e/ou caracteres especiais.

## Dependências e Instalações
- Para rodar a aplicação, é necessário ter instalado alguns pré-requisitos, conforme mostra abaixo: 
    - Interpretador do Python 3;
    - Node.js;
    - npm;
    - Dependências Node: Para baixar as dependencias node, basta entrar na pasta do projeto com o cmd e executar o comando "npm install".

## Uso

### Preparando a aplicação
- Para utilizar a ferramenta, é necessário utilizar alguma ferramenta de envio de requisição para API, como o Insomnia ou o Postman. 
- Abra o projeto no cmd e execute a função "npm run dev". Após isso, irá aparecer uma mensagem "API disponível em: localhost:3400. 
- Coloque a url localhost3400 na ferramento de envio (insomnia) e envie uma requisição GET para testar. Caso esteja tudo certo aparecerá a mensagem "API Rodando, por favor, coloque a rota "/gerar" para testar a aplicação.".

### Gerando a senha 
- Coloque a rota /gerar na URL e em seguida, configure o body da requisição com as instruções abaixo.
- A requisição utiliza parâmetros passados em JSON e segue o seguinte formato de exemplo: 

{
    "quantidade" : 8,
    "numero": "s",
    "maiusculo": "s",
    "minusculo": "s",
    "simbolo": "n"
}
- "quantidade" se refere ao número de caractéres que a senha irá compor; 
- "numero" diz se a senha possuirá números ("s") ou não ("n"); 
- "maiusculo" diz se a senha possuirá letras maiusculas ("s") ou não ("n");
- "minusculo" diz se a senha possuirá letras minusculo ("s") ou não ("n");
- "simbolo" diz se a senha possuirá simbolos ("s") ou não ("n");

- Agora é só colocar os parâmetros conforme informado acima e enviar um GET para essa rota, que a API retornará uma senha com a quantidade de caracteres solicitados.

## Estrutura do projeto
- Essa ferramenta utilizou a estrutura de pastas padrão de API Rest com Node.js; 

- No escopo principal, temos o arquivo "server.js" que disponibiliza a API na porta 3400 do localhost.
- Na pasta src, temos o arquivo "app.js", que define as rotas da API e chama as validações dos parâmetros informados no body. 
- Na pasta code, temos 3 arquivos: 
    - ValidarParam.js: Verifica se todos os parâmetros necessários foram informados, para evitar erros ao chamar o gerador. 
    - callGerador.js: Executa comandos shell (através da biblioteca shelljs) para executar o gerador de senhas.
    - gerador.py: Código em python que cria a senha conforme os parâmetros informados. 
