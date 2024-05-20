# Encontrar Palavras Similares

## Visão geral do script

Este repositório contém scripts em Python que permitem encontrar palavras semelhantes usando modelos pré-treinados de Word2Vec e FastText. Os scripts carregam ou baixam os modelos e permitem que você insira palavras para obter uma lista de palavras semelhantes com suas respectivas similaridades.

## Funcionalidades

- Carregar ou baixar automaticamente o modelo Word2Vec ou o FastText pré-treinado.
- Permite que o usuário insira palavras e obtenha palavras semelhantes.
- Armazena o modelo localmente para evitar downloads repetidos.
- Interface simples de linha de comando para interação fácil.

## Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

Você pode instalar e configurar o script de três maneiras diferentes: download direto, usando Git ou Github Desktop.

### Download Direto

1. Baixe o arquivo do script diretamente.
2. Salve-o em um diretório de sua escolha.

### Usando Git

1. Clone o repositório em seu computador:
   ```sh
   git clone https://github.com/profmatheuspassos/encontrar-palavras-similares
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd encontrar-palavras-similares
   ```

### Usando Github Desktop

1. Abra o Github Desktop.
2. Vá para `File > Clone Repository`.
3. Insira a URL do repositório: `https://github.com/profmatheuspassos/encontrar-palavras-similares`.
4. Clique em `Clone`.

## Uso

1. Navegue até o diretório do projeto no terminal.
2. Instale as dependências necessárias:
   ```sh
   pip install gensim==4.3.2 scipy==1.9.3
   ```

### Para usar o script Word2Vec

1. Execute o script `similar_words-Word2Vec.py`:
   ```sh
   python similar_words-Word2Vec.py
   ```
2. Siga as instruções na tela. Digite uma palavra para encontrar palavras semelhantes ou digite "fim" para terminar.

### Para usar o script FastText

1. Execute o script `similar-words-FastText.py`:
   ```sh
   python similar-words-FastText.py
   ```
2. Siga as instruções na tela. Digite uma palavra para encontrar palavras semelhantes ou digite "fim" para terminar.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Por favor, siga as diretrizes de contribuição do projeto.

## Observações

- Certifique-se de que você tem uma conexão de internet ativa na primeira vez que executar os scripts para que eles possam baixar os modelos Word2Vec e FastText.
- Os modelos pré-treinados são grandes (cerca de 1.5GB cada), então o download pode levar algum tempo dependendo da sua conexão.
- O modelo Word2Vec será salvo na pasta `models` com o nome `word2vec-google-news-300`.
- O modelo FastText será salvo na pasta `models` com o nome `fasttext-wiki-news-subwords-300`.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Isenção de responsabilidade

Este script e os modelos de dados usados são fornecidos "como estão", sem garantias de qualquer tipo, expressas ou implícitas, incluindo, mas não se limitando a, garantias de comercialização, adequação a um propósito específico e não violação. O uso dos scripts é de sua responsabilidade.

---

Esperamos que estes scripts sejam úteis para seus projetos de processamento de linguagem natural. Se tiver alguma dúvida ou sugestão, por favor, entre em contato!