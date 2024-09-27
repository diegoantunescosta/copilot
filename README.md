# Aplicação de Chatbot usando o Modelo Llama3

## Visão Geral
Este projeto é um chatbot simples que interage com uma API baseada no modelo Llama3 para gerar respostas a partir de entradas do usuário. A aplicação utiliza uma API REST para se comunicar com o modelo e obter as respostas. A interação é projetada para simular uma sessão de chat entre o usuário e um assistente de IA.

## Funcionalidades
Respostas em Tempo Real: O chatbot imprime as respostas progressivamente à medida que são recebidas da API.
Interação com o Usuário: O usuário pode inserir perguntas ou comandos, e o chatbot responde com base nas mensagens enviadas ao modelo.
Histórico de Conversa: O chatbot mantém o histórico da conversa, enviando-o com cada nova mensagem para manter o contexto.
Tratamento de Erros: Qualquer erro retornado pela API é capturado e tratado como exceção.

## Requisitos
Python 3.x
Biblioteca requests para lidar com as requisições à API.
Instância em execução do modelo Llama3 na API em http://0.0.0.0:11434/api/chat.
Para instalar as bibliotecas necessárias, execute:

```bash

pip install requests
````

## Estrutura do Arquivo
main.py: Arquivo principal que contém a lógica do chatbot.

chat(): Função responsável por enviar as mensagens para a API e processar as respostas.

main(): Função que inicia a interação com o usuário, recebe os prompts e gerencia o fluxo da conversa.

Como Executar

Clone este repositório para sua máquina local.

Certifique-se de que a API do modelo Llama3 esteja rodando em http://0.0.0.0:11434/api/chat.

Execute o script Python:

```bash
python main.py
```
Insira suas perguntas ou comandos no terminal e veja as respostas do assistente de IA.
Exemplo de Uso
bash

Enter a prompt: Qual é a capital da França?

Resposta: A capital da França é Paris.

## Tratamento de Erros

Se a API retornar algum erro, o script levantará uma exceção com a mensagem de erro correspondente, permitindo uma depuração mais fácil.

Contribuição
Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades, abrindo pull requests ou issues.
