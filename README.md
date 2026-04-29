# DW2 Lore Scraper

Ferramenta para extrair conversas do Discord do servidor Drunken Wrestlers 2 e converter em arquivos TXT para análise no NotebookLM.

## 📋 Pré-requisitos

- Python 3.7+
- [DiscordChatExporter CLI](https://github.com/Tyrrrz/DiscordChatExporter/releases)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/dw2-lore-scraper.git
cd dw2-lore-scraper
```

2. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

3. Baixe o DiscordChatExporter CLI:
   - Acesse: https://github.com/Tyrrrz/DiscordChatExporter/releases
   - Baixe a versão CLI para Windows
   - Extraia na pasta `scripts/`

4. Configure suas credenciais:
   - Copie `config/config.example.txt` para `config/config.txt`
   - Preencha com seu token do Discord

## 🔑 Como obter o token do Discord

1. Abra o Discord no navegador
2. Pressione `F12` para abrir o DevTools
3. Vá na aba **Network**
4. Filtre por "messages"
5. Copie o valor do header `Authorization`

## 📖 Uso

### 1. Exportar mensagens do Discord

Execute o script de exportação:

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
- Ler o arquivo JSON exportado
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

## 📁 Estrutura do Projeto

```
dw2-lore-scraper/
├── scripts/
│   ├── export_discord.bat      # Script de exportação
│   ├── extrair_txt.py          # Converte JSON → TXT
│   └── dividir_txt.py          # Divide TXT em partes menores
├── config/
│   └── config.example.txt      # Template de configuração
├── output/                     # Arquivos gerados (não versionado)
├── requirements.txt            # Dependências Python
└── README.md
```

## ⚙️ Configuração

Edite `scripts/export_discord.bat` para ajustar:

- `TOKEN`: Seu token do Discord
- `CHANNEL_ID`: ID do canal a ser exportado
- `DATA_INICIO`: Data inicial (formato: YYYY-MM-DD)
- `DATA_FIM`: Data final (formato: YYYY-MM-DD)

## 📊 IDs dos Canais DW2

- Chat ENG: `465332971369660419`
- Chat Russo: `465357353966108685`

## ⚠️ Avisos

- **Não compartilhe seu token do Discord**
- O processo de exportação pode levar várias horas devido aos rate limits
- Mantenha o PC ligado durante a exportação (pode desligar a tela)
- Arquivos JSON podem ser muito grandes (500MB+)

## 🔗 Links Úteis

- [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter)
- [NotebookLM](https://notebooklm.google.com/)
- [Servidor Discord DW2](https://discord.gg/dw2)

## 📝 Licença

MIT
