# CLI(Interface de comando) Globocard

Esse projeto é um CLI desenvolvido em Python para ser utilizado em conjunto com a Api GloboCard e foi desenvolvido para o desafio Globo. Com objetivo de facilitar o processo de exportação de Cards esportivos(Insights) de um arquivo CSV para a API GloboCard. Sendo possível criar cards e suas respectivas tags em um único comando.

## Requerimentos:

- Python 3.x

## Primeiros passos
1. Clone esse repositório em um local de fácil localização
2. Acesse a pasta raíz do projeto clonado.
3. Crie um arquivo .env na raíz do projeto e adicione as seguintes linhas:

        #VOCÊ PODE UTILIZAR A URL DE PRODUÇÃO DA API GLOBOCARD:
        #https://api-globo-card.herokuapp.com/
        API_URL=http://127.0.0.1:5000

4. Abra um terminal na raíz do projeto.
5. Crie um arquivo csv e insira as seguintes linhas:


        text,tag
        Lorem ipsum dolor sit amet., Futebol
        Mauris fringilla non quam vel lacinia,Natação
        Mauris fringilla non quam vel lacinia,Olimpiadas
        Cras in tempus libero


6. Execute o comando <b>python cli.py</b>
7. Digite o nome do arquivo CSV sem a extensão no final