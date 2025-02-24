# AI Lawyer - Legal Assistance with RAG and DeepseekR1

##  Overview
AI Lawyer is an advanced legal assistant powered by Retrieval-Augmented Generation (RAG) using LangChain, Ollama, QROQ, UV, and Streamlit. It leverages AI agents to provide legal insights, analyze documents, and assist users with legal queries efficiently.

## 🛠️ Features
- **RAG-based legal assistance** for retrieving relevant legal documents and cases.
- **AI-powered legal document analysis** using LangChain, QROQ, and UV.
- **Ollama for local model execution**, ensuring privacy and control.
- **Streamlit UI** for an intuitive and interactive user experience.

## 🏗️ Tech Stack
- **[LangChain](https://python.langchain.com/)** - Framework for building LLM-based applications.
- **[Ollama](https://ollama.ai/)** - Run AI models locally.
- **[QROQ](https://qroq.ai/)** - Advanced document retrieval system.
- **[UV](https://github.com/yourusername/uv)** - High-performance server framework.
- **[Streamlit](https://streamlit.io/)** - Web UI framework for AI applications.
- **Python, Deepseek models, and more.**

## 🚀 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ankitvishwakarmaml/AI-Lawyer-chatbot-with-DeepseekR1.git
cd AI-Lawyer-chatbot-with-DeepseekR1
```
### 2️⃣ Install UV and Dependencies
```bash
pip install uv
uv sync
```
### 3️⃣ Run the Application
```bash
uvicorn server.main:app --reload &
streamlit run frontend.py
```

## 🎯 Usage
1. **Upload legal documents** or enter queries.
2. **AI retrieves relevant legal information** using RAG.
4. **Interact with AI Lawyer via the Streamlit UI.**

## 🤝 Contributing
Feel free to submit pull requests or report issues. Contributions are welcome!

## 📜 License
This project is licensed under the MIT License.

---
💡 *Empowering legal professionals with AI-driven insights!*


