# Resolução Gráfica do Simplex

Este é um projeto que utiliza Flask para criar uma API que gera um gráfico de resolução gráfica do Simplex. O gráfico é gerado usando a biblioteca pygal.

## Pré-requisitos

Certifique-se de ter o Python e as bibliotecas Flask, pygal e flask-cors instaladas em seu ambiente de desenvolvimento.

## Instalação

1. Clone este repositório para o seu ambiente local.

git clone https://github.com/Thiafa/api-graphic.git

2. Navegue até o diretório do projeto.

cd simplex-grafico

3. Instale as dependências usando o pip.

pip install -r requirements.txt


## Uso

1. Inicie o servidor Flask executando o arquivo `app.py`.

python app.py


2. Acesse a API em `http://localhost:5000/api` para verificar se o servidor está em execução corretamente.

3. Faça uma solicitação POST para `http://localhost:5000/api/grafico` com os seguintes parâmetros no corpo da solicitação:

- `constraints`: Um objeto JSON que contém as restrições para o problema do Simplex. Cada restrição é representada por uma chave única e possui as seguintes propriedades:
  - `vars`: Um array de valores numéricos que representa os coeficientes das variáveis na restrição.
  - `result`: Um valor numérico que representa o resultado da restrição.

- `x_optimal`: Um array contendo as coordenadas ótimas (x, y) para o ponto de otimização do gráfico. 

- `z_optimal`: Um valor numérico que representa o valor ótimo da função objetivo Z. 

- `function_main`: Um array de valores numéricos que representa a função objetivo principal do problema do Simplex.

4. A API retornará a imagem do gráfico gerado em formato SVG.

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para enviar um pull request. Todas as contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a licença MIT. 
