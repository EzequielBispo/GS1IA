# Projeto de Detecção de Coral

## Visão Geral

Este projeto utiliza a biblioteca FastAPI para criar uma API de detecção de corais utilizando um modelo treinado no Roboflow. A API recebe imagens, realiza a detecção de corais e retorna informações detalhadas sobre as detecções.

## Link do Modelo no Roboflow

[Corais Object Detection](https://universe.roboflow.com/bxspoworkspace/corais)

## Estrutura do Projeto

- **index.py**: Contém o código principal da API.
- **requirements.txt**: Lista das dependências necessárias para executar o projeto.

## Dependências

- `fastapi`
- `uvicorn`
- `opencv-python`
- `numpy`
- `roboflow`

## Instalação

1. Clone o repositório.

```sh
git clone 
```

2. Instale as dependências.

```sh
pip install -r requirements.txt
```

## Configurando o Insomnia para Testar o Endpoint

1. **Criar uma Nova Requisição**:
   - **Nome**: `Detect Coral`
   - **Método**: `POST`
   - **URL**: `http://localhost:8000/detect-coral/`

2. **Configurar o Corpo da Requisição**:
   - **Tipo**: `Multipart Form`
   - **Key**: `file`
   - **Value**: Selecione o arquivo de imagem

3. **Enviar a Requisição**: Clique em "Send" e verifique a resposta JSON.
