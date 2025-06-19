<div align="center"> 
<h1>🤖 CodeaBot - AI Chat Assistant</h1> 
  
<p>An intelligent chatbot built with Streamlit and OpenAI GPT, developed to provide friendly and helpful assistance in various tasks.</p>

</div>

[🇧🇷 Portuguese Version](README-pt.md)



![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![OpenAI](https://img.shields.io/badge/openai-v1.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

--- 

## 📋 Table of Contents

- [Features](README.md#-features)
- [Technologies](README.md#-technologies)
- [Demo](README.md#-demo)
- [Installation](README.md#-installation)
- [Configuration](README.md#-configuration)
- [Troubleshooting](README.md#-troubleshooting)
- [Contributing](README.md#-contributing)
- [Roadmap](README.md#-roadmap)
- [License](README.md#-license)
- [Author](README.md#-author)
- [Acknowledgments](README.md#-acknowledgments)

## ✨ Features

- 🎯 **Intuitive Interface**: Modern interface built with Streamlit
- 🔐 **Security**: Support for custom API keys with validation
- ⚙️ **Configurable**: Adjust model, temperature and tokens
- 💬 **Real-time Chat**: Response streaming with visual indicators
- 📱 **Responsive**: Adaptive layout for different devices
- 🗂️ **Persistent History**: Maintains conversations during session
- 🎨 **Modern UI/UX**: Clean design with emojis and colors
- 🔧 **Advanced Logging**: Log system for debugging and monitoring

### Main Features

#### 💬 Basic Chat
- Type your message in the bottom field
- Press Enter or click the send icon
- Wait for the real-time response

#### ⚙️ Settings
- Model: Choose between gpt-3.5-turbo, gpt-4, etc.
- Creativity: Adjust from 0.0 (conservative) to 1.0 (creative)
- Tokens: Token limit per response (100-2000)

#### 🗑️ Management
- Clear Chat: Remove all history
- History: View previous conversations
- Status: Monitor connection and messages

#### Supported Models
- gpt-3.5-turbo: Fast and efficient
- gpt-4: More accurate and capable
- gpt-4-turbo: Optimized speed

## 🛠️ Technologies
|Technology	|Version	|Purpose|
------------|-------|---------|
|Python	|3.8+	|Main language
|Streamlit|	1.28+	|Web interface
|OpenAI	|1.0+	|AI API
|python-dotenv|	1.0+	|Variable management
|typing	|Built-in	|Type hints
|logging	|Built-in	|Log system



## 🎬 Demo

<div align="center">
  <img src="assets/chat-demo.gif" alt="Chat Demo" width="500">
</div>


## 🚀 Local Installation and Usage

### Prerequisites

- Python 3.8 or higher
- OpenAI account with API key

### Step by Step

1. **Clone the repository**
```bash
git clone https://github.com/your-username/codeabot.git
cd codeabot
```
2. **Create a virtual environment**
```bash
py -3.11 -m venv .venv

# Windows
.venv\Scripts\Activate.ps1 (PowerShell)
.venv\Scripts\Activate.bat (CMD)

# macOS/Linux
source .venv/bin/activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the application**
```bash
streamlit run codeabot.py
```

## ⚙️ Configuration
### **Option 1**: .env File (Recommended)
Create a .env file in the project root:

env
```bash
OPENAI_API_KEY=sk-proj-your-key-here
```

### **Option 2**: Web Interface
- Run the application
- Enter your API key in the sidebar field
- Click "Validate API Key"

### Get OpenAI API Key
- Access [platform.openai.com](https://platform.openai.com/api-keys)
- Log into your account
- Click "Create new secret key"
- Copy the key (starts with sk-)

## 🐛 Troubleshooting
### Common Issues
- ❌ "Invalid API Key"
  - Solution: Check if your API key is correct and has available credits.
- ❌ "Rate limit exceeded"
  - Solution: Wait a few minutes before making new requests.
- ❌ "Connection error"
  - Solution: Check your internet connection.
 

## 🤝 Contributing

### Contributions are welcome! Follow these steps:
1. **Fork** the project
2. **Create** a **branch** for your feature (git checkout -b feature/AmazingFeature)
3. **Commit** your changes (git commit -m 'Add some AmazingFeature')
4. **Push** to the **branch** (git push origin feature/AmazingFeature)
5. **Open** a **Pull Request**

### Contributing Guidelines
- Follow existing code patterns
- Add tests for new features
- Update documentation when necessary
- Use type hints in all functions
- Keep commits small and descriptive

## 📝 Roadmap
- [ ] Support for multiple conversations
- [ ] Conversation export
- [ ] Customizable themes
- [ ] Support for images and files
- [ ] Integration with other AI models
- [ ] Plugin system
- [ ] Offline mode with local models

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## 👨‍💻 Author
### André Codea 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230570a8?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/andrecodea/) [![GitHub](https://img.shields.io/badge/GitHub-%23121011?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/andrecodea)

*Computer Science Student at **UNESA***

## 🙏 Acknowledgments
- [OpenAI](https://www.openai.com) for the API.
- [Streamlit](https://www.streamlit.io) for the web framework
- **Python Community** for support and resources.
