# Discord Chat Scraper

Ferramenta para extrair conversas de qualquer servidor Discord e converter em arquivos TXT para análise no NotebookLM.

## Pré-requisitos

- Python 3.7+
- [DiscordChatExporter CLI](https://github.com/Tyrrrz/DiscordChatExporter/releases)

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/JBRYAN333/discord-chat-scrapper.git
cd discord-chat-scrapper
```

### 2. Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 3. Baixe o DiscordChatExporter CLI

- Acesse: https://github.com/Tyrrrz/DiscordChatExporter/releases
- Baixe a versão **CLI** para Windows (arquivo `DiscordChatExporter.Cli.win-x64.zip`)
- Extraia o conteúdo do ZIP
- Copie o arquivo `DiscordChatExporter.Cli.exe` para a pasta `scripts/` deste projeto

**Estrutura esperada:**
```
discord-chat-scrapper/
├── scripts/
│   ├── DiscordChatExporter.Cli.exe   <-- coloque aqui
│   ├── export_discord.bat
│   ├── extrair_txt.py
│   └── dividir_txt.py
├── config/
├── output/
├── requirements.txt
└── README.md
```

### 4. Configure o script de exportação

Abra o arquivo `scripts/export_discord.bat` em um editor de texto e altere as variáveis no início do arquivo:

```batch
SET TOKEN=SEU_TOKEN_AQUI
SET CHANNEL_ID=SEU_CHANNEL_ID_AQUI
SET DATA_INICIO=2024-01-01
SET DATA_FIM=2024-12-31
```

**O que colocar em cada campo:**

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `TOKEN` | Seu token de autorização do Discord | `Njg4NTI5NzQyNjIxNzA0MzUw.xxxxx.xxxxx` |
| `CHANNEL_ID` | ID do canal a ser exportado | `465332971369660419` |
| `DATA_INICIO` | Data inicial das mensagens | `2024-01-01` |
| `DATA_FIM` | Data final das mensagens | `2024-12-31` |

## Como obter o token do Discord

1. Abra o Discord no navegador (discord.com/app)
2. Pressione `F12` para abrir as ferramentas de desenvolvedor
3. Vá na aba **Network**
4. Filtre por "messages" ou faça qualquer ação no Discord
5. Clique em uma requisição
6. Vá em **Headers** → **Request Headers**
7. Copie o valor do campo `Authorization`

## Como obter o ID do canal

1. No Discord, vá em **Configurações** → **Avançado** → ative **Modo de Desenvolvedor**
2. Clique com o botão direito no canal desejado
3. Selecione **Copiar ID do Canal**

## Uso

### 1. Exportar mensagens do Discord

```bash
cd scripts
export_discord.bat
```

Isso irá:
- Exportar mensagens do canal configurado
- Salvar em formato JSON na pasta `output/`
- Respeitar rate limits do Discord (pode levar várias horas)

### 2. Converter JSON para TXT

```bash
cd scripts
python extrair_txt.py
```

Isso irá:
- Ler o arquivo JSON exportado (deve estar na mesma pasta do script ou em `output/`)
- Extrair mensagens em formato legível
- Salvar em chunks de 10.000 mensagens em `output/txt_partes/`

### 3. Dividir para NotebookLM (opcional)

Se os arquivos TXT forem muito grandes (>3MB):

```bash
cd scripts
python dividir_txt.py
```

Isso irá:
- Dividir arquivos em partes de até 3MB
- Salvar em `output/txt_partes_notebooklm/`
- Pronto para upload no NotebookLM

## Estrutura do Projeto

```
discord-chat-scrapper/
├── scripts/
│   ├── DiscordChatExporter.Cli.exe   # CLI do DiscordChatExporter (baixar separadamente)
│   ├── export_discord.bat            # Script de exportação
│   ├── extrair_txt.py                # Converte JSON → TXT
│   └── dividir_txt.py                # Divide TXT em partes menores
├── config/
│   └── config.example.txt            # Exemplo de configuração (opcional)
├── output/                           # Arquivos gerados (não versionado)
│   └── txt_partes/                   # Arquivos TXT extraídos
├── requirements.txt                  # Dependências Python
└── README.md
```

## Avisos

- **Não compartilhe seu token do Discord** - ele dá acesso total à sua conta
- O processo de exportação pode levar várias horas devido aos rate limits
- Mantenha o PC ligado durante a exportação (pode desligar a tela)
- Arquivos JSON podem ser muito grandes (500MB+)
- O token expira eventualmente - se der erro de autenticação, pegue um novo

## Links Úteis

- [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter)
- [NotebookLM](https://notebooklm.google.com/)

## Licença

MIT
