# 🤖 CodeaBot - AI Chat Assistant

[🇺🇸 English Version](README.md)

Um chatbot inteligente construído com Streamlit e OpenAI GPT, desenvolvido para fornecer assistência amigável e útil em diversas tarefas.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![OpenAI](https://img.shields.io/badge/openai-v1.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

--- 

## 📋 Índice

- [Características](#-características)
- [Demonstração](#-demonstração)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias](#-tecnologias)
- [Configurações Avançadas](#-configurações-avançadas)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Autor](#-autor)

## ✨ Características

- 🎯 **Interface Intuitiva**: Interface moderna construída com Streamlit
- 🔐 **Segurança**: Suporte para API keys personalizadas com validação
- ⚙️ **Configurável**: Ajuste de modelo, temperatura e tokens
- 💬 **Chat em Tempo Real**: Streaming de respostas com indicadores visuais
- 📱 **Responsivo**: Layout adaptável para diferentes dispositivos
- 🗂️ **Histórico Persistente**: Mantém conversas durante a sessão
- 🎨 **UI/UX Moderna**: Design limpo com emojis e cores
- 🔧 **Logging Avançado**: Sistema de logs para debugging e monitoramento


## Funcionalidades Principais

### 💬 Chat Básico
- Digite sua mensagem no campo inferior
- Pressione Enter ou clique no ícone de envio
- Aguarde a resposta em tempo real

### ⚙️ Configurações
- Modelo: Escolha entre gpt-3.5-turbo, gpt-4, etc.
- Criatividade: Ajuste de 0.0 (conservador) a 1.0 (criativo)
- Tokens: Limite de tokens por resposta (100-2000)

### 🗑️ Gerenciamento
- Limpar Chat: Remove todo o histórico
- Histórico: Visualize conversas anteriores
- Status: Monitore conexão e mensagens


## 🎬 Demonstração

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Conta OpenAI com API key

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/codeabot.git
cd codeabot
```
2. **Crie um ambiente virtual**
```bash
py -3.11 -m venv .venv

# Windows
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/Activate.bat
```
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
4. **Execute a aplicação**
```bash
streamlit run .\codeabot.py
```

## ⚙️ Configuração
### Opção 1: Arquivo .env (Recomendado)
Crie um arquivo .env na raiz do projeto:

env
```bash
OPENAI_API_KEY="SUA CHAVE"
```

### Opção 2: Interface Web
- Execute a aplicação
- Insira sua API key no campo da sidebar
- Clique em "Validate API Key"

### Obter API Key da OpenAI
- Acesse [platform.openai.com]
- Faça login em sua conta
- Clique em "Create new secret key"
- Copie a chave (começa com sk-)

## 🐛 Solução de Problemas
### Problemas Comuns
- ❌ "Invalid API Key"
  - Solução: Verifique se sua API key está correta e tem créditos disponíveis.
- ❌ "Rate limit exceeded"
  - Solução: Aguarde alguns minutos antes de fazer novas requisições.
- ❌ "Connection error"
  - Solução: Verifique sua conexão com a internet.
 

---

## 🤝 Contribuição

### Contribuições são bem-vindas! Siga estes passos:
- Fork o projeto
- Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
- Commit suas mudanças (git commit -m 'Add some AmazingFeature')
- Push para a branch (git push origin feature/AmazingFeature)
- Abra um Pull Request

### Diretrizes de Contribuição
- Siga o padrão de código existente
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário
- Use type hints em todas as funções
- Mantenha os commits pequenos e descritivos

## 📝 Roadmap
- [ ] Suporte para múltiplas conversas
- [ ] Exportação de conversas
- [ ] Temas personalizáveis
- [ ] Suporte para imagens e arquivos
- [ ] Integração com outros modelos de IA
- [ ] Sistema de plugins
- [ ] Modo offline com modelos locais

## 📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE.txt) para detalhes.

## 👨‍💻 Autor
### André Codea [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230570a8?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/andrecodea/) [![GitHub](https://img.shields.io/badge/GitHub-%23121011?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/andrecodea)
- Estudante de Ciência da Computação na **UNESA**

## 🙏 Agradecimentos
- [OpenAI](https://www.openai.com) pela API.
- [Streamlit](https://www.streamlit.io) pelo framework web
- Comunidade Python pelo suporte e recursos.

---
⭐ Se este projeto foi útil para você, considere dar uma estrela!
