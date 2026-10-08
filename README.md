# Generative AI Projects

A collection of practical Generative AI projects built with **Python, Large Language Models (LLMs), LangChain, LangGraph, RAG, AI Agents, and Streamlit**.

This repository documents my hands-on journey toward becoming a **Generative AI Developer**, with a focus on building practical applications and understanding how modern GenAI systems work.

---

## About Me

I am an IT professional with experience in technical support and service desk operations, currently transitioning into **Generative AI development**.

I am building hands-on projects using Python and modern GenAI technologies, with a focus on:

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Agentic RAG
* AI Agents
* LangChain
* LangGraph
* LLM APIs
* Streamlit
* SQL + AI applications
* Data validation with Pydantic

My goal is to build practical GenAI applications and transition into a **Generative AI Developer / AI Engineer** role.

---

# Featured Projects

These are the main projects in this repository that demonstrate my practical GenAI development journey.

---

## 1. End-to-End Agentic RAG Chatbot

**File:** `apps/5_rag_agent.py`

### Problem

Users may have information spread across multiple PDF documents and need a simple way to ask questions about that information without manually searching through the documents.

### Solution

Built a Streamlit-based **Agentic RAG chatbot** that allows users to upload multiple PDF documents and ask questions about their content.

The application processes the uploaded documents, creates embeddings, stores them in an in-memory vector store, and provides the agent with a retrieval tool that it can use to obtain relevant document context.

### Technologies

**Python | LangChain | LangGraph | RAG | OpenAI Embeddings | Groq | Streamlit | PyPDF**

### Why these components?

* **PyPDFDirectoryLoader** — loads PDF documents from the document directory.
* **RecursiveCharacterTextSplitter** — divides documents into smaller chunks for efficient retrieval.
* **OpenAI Embeddings** — converts document chunks into numerical vector representations.
* **InMemoryVectorStore** — stores embeddings and enables similarity search.
* **Retriever Tool** — allows the AI agent to search the uploaded documents.
* **LangChain Agent** — coordinates the LLM and retrieval tool.
* **ChatGroq** — provides the language model used by the agent.
* **InMemorySaver** — provides checkpoint support for the agent.
* **Streamlit** — provides the interactive chat interface.

### Workflow

```text
User uploads PDF files
        |
Load PDF documents
        |
Split documents into chunks
        |
Create embeddings
        |
Store embeddings in InMemoryVectorStore
        |
Create retrieval tool
        |
Create AI Agent
        |
User asks a question
        |
Agent uses retrieval tool
        |
Retrieve relevant document context
        |
LLM generates answer
        |
Answer displayed in Streamlit
```

### Key Concepts Learned

* Retrieval-Augmented Generation
* Vector embeddings
* Similarity search
* AI Agents
* Tool calling
* Agent checkpointing
* Document processing
* Streamlit application development

---

## 2. Agentic RAG System

**File:** `notebooks/14_rag_ai_agent.ipynb`

### Problem

A traditional RAG pipeline generally follows a fixed sequence of retrieving information and generating an answer.

### Solution

Built an **Agentic RAG system** to understand how AI agents can be incorporated into a retrieval workflow.

The project focuses on understanding how an agent can use tools and reasoning to retrieve information before generating a response.

### Technologies

**Python | LangChain | RAG | AI Agents | LLMs**

### Key Concepts Learned

* Agentic RAG
* AI agent workflows
* Retrieval
* Tool usage
* LLM reasoning
* Combining agents with RAG

### High-Level Workflow

```text
User Question
      |
   AI Agent
      |
Determine required action
      |
Retrieve relevant information
      |
Process retrieved context
      |
     LLM
      |
Final Answer
```

---

## 3. SQL AI Agent / Task Manager

**File:** `apps/4_sql_agent.py`

### Problem

Interacting with a database normally requires users to understand SQL syntax and manually write queries.

### Solution

Built an AI-powered **Task Manager** that allows users to interact with a SQLite database using natural language.

The AI agent has access to SQL database tools and can perform task-related CRUD operations such as creating, reading, updating, and deleting tasks.

### Technologies

**Python | LangChain | SQL | SQLite | SQLDatabaseToolkit | Ollama | LangGraph | Streamlit**

### Why these components?

* **SQLite** — provides a lightweight relational database.
* **SQLDatabase** — connects the application to the database.
* **SQLDatabaseToolkit** — provides tools for interacting with the SQL database.
* **Ollama** — runs the LLM locally.
* **Llama 3.2 3B** — used as the local language model.
* **LangChain Agent** — allows the LLM to use database tools.
* **InMemorySaver** — provides checkpoint support.
* **Streamlit** — provides the task management chat interface.

### Workflow

```text
User gives natural-language request
              |
          AI Agent
              |
    Understand database schema
              |
       Select SQL tool
              |
       Generate SQL query
              |
       Execute SQL query
              |
      Analyze the result
              |
        Final response
```

### Supported Operations

* CREATE tasks
* READ tasks
* UPDATE tasks
* DELETE tasks
* Query task status
* Retrieve recent tasks

### Key Concepts Learned

* SQL agents
* Natural-language-to-SQL
* Database tools
* Database schema understanding
* CRUD operations
* Local LLMs with Ollama
* Tool-based AI agents

---

## 4. RAG-Based PDF Q&A Chatbot

**Files:**

* `notebooks/12_vector_embeddings.ipynb`
* `notebooks/13_rag_based_pdf_qna_bot.ipynb`

### Problem

Finding specific information inside large PDF documents manually can be time-consuming.

### Solution

Built a **Retrieval-Augmented Generation (RAG) based PDF Q&A system** that loads documents, splits the content into chunks, creates embeddings, stores them in a vector database, retrieves relevant information, and uses an LLM to generate an answer.

### Technologies

**Python | LangChain | RAG | Embeddings | Chroma | PyPDF | LLMs**

### Workflow

```text
PDF Document
     |
Load Document
     |
Split Text
     |
Create Embeddings
     |
Store in Vector Database
     |
User Question
     |
Similarity Search
     |
Retrieve Relevant Context
     |
LLM
     |
Generated Answer
```

### Key Concepts Learned

* Document loading
* Text splitting
* Embeddings
* Vector databases
* Similarity search
* Retrieval
* RAG architecture
* Context-based generation

---

# Supporting Projects

## LangGraph Fundamentals

## LangGraph Q&A Chatbot with Memory

**Files:**

* `apps/6_langgraph_qna_bot.py`
* `notebooks/17_langgraph_qna_bot.ipynb`

### Problem

A basic LLM application can answer individual questions, but it does not automatically provide a structured way to maintain conversation state across multiple interactions.

### Solution

Built a **stateful Q&A chatbot using LangGraph** that maintains conversation context through graph state and checkpoint-based memory.

The application uses a LangGraph `StateGraph` to define the conversation workflow. A custom `ChatState` model stores the message history, while the `add_messages` reducer manages the addition of user and AI messages.

The chatbot uses **GPT OSS 20B through Groq** to generate responses and `InMemorySaver` to maintain checkpointed conversation state.

### Technologies

**Python | LangGraph | LangChain | Groq | GPT OSS 20B | Pydantic | InMemorySaver**

### Why these components?

* **Pydantic `BaseModel`** - defines the structured `ChatState` used by the graph.
* **`Annotated[list, add_messages]`** - manages and updates the conversation message history.
* **LangGraph `StateGraph`** - defines the stateful chatbot workflow.
* **ChatBot Node** - receives the current graph state and invokes the LLM.
* **ChatGroq** - connects the application to the GPT OSS 20B model through Groq.
* **`InMemorySaver`** - provides checkpoint-based memory for the graph.
* **Thread ID** - identifies the conversation thread when invoking the graph.

### Workflow

```text
User Question
      |
      v
ChatState
      |
      v
LangGraph StateGraph
      |
      v
ChatBot Node
      |
      v
GPT OSS 20B via Groq
      |
      v
AI Response
      |
      v
add_messages
      |
      v
Checkpoint Memory
      |
      v
Next Conversation Turn
```

### Graph Structure

The chatbot uses a simple LangGraph workflow:

```text
START
  |
  v
ChatBot Node
  |
  v
END
```

The `ChatBot Node` receives the current conversation state, sends the messages to the LLM, and returns the updated state.

### Key Concepts Learned

* LangGraph `StateGraph`
* Graph state management
* Nodes and edges
* `START` and `END`
* Message reducers
* `add_messages`
* Stateful LLM applications
* Conversation memory
* Checkpointing with `InMemorySaver`
* Thread-based conversation state
* Integrating LLMs into LangGraph workflows

### Learning Progression

This project builds on the previous **LangGraph Fundamentals** project by moving from understanding basic graph structures to building a practical stateful chatbot.

```text
LangGraph Fundamentals
          |
          v
StateGraph + Nodes + Edges
          |
          v
Chat State + Message History
          |
          v
Checkpoint Memory
          |
          v
Stateful Q&A Chatbot
```


**File:** `notebooks/16_basic_langgraph.ipynb`

Explored the fundamentals of **LangGraph** and graph-based workflows for building structured AI applications.

### Concepts

* Graphs
* Nodes
* Edges
* State
* Workflow execution
* Multi-step AI systems

---

## Pydantic Data Validation

**File:** `notebooks/15_pydantic_data_validation.ipynb`

Explored **Pydantic** for creating structured data models and validating data in Python applications.

### Concepts

* Data models
* Type validation
* Structured data
* Input validation
* Reliable data handling

---

## Q&A Bot

**File:** `apps/1_QNA_bot.py`

Built an LLM-powered Q&A application to understand the fundamentals of interacting with LLMs from Python.

### Concepts

* LLM APIs
* Prompting
* `llm.invoke()`
* Environment variables
* Streamlit

---

## AI Agents

**File:** `apps/2_google_agents.py`

Explored the fundamentals of AI agents and how LLMs can interact with external tools to perform tasks.

### Concepts

* AI Agents
* Tools
* LLM reasoning
* External information retrieval
* Agent workflows

---

# Technical Skills

### Programming

* Python

### Generative AI

* Large Language Models (LLMs)
* Prompt Engineering
* LLM APIs
* AI Agents
* Agentic AI

### RAG

* Document Loading
* Text Splitting
* Embeddings
* Vector Databases
* Similarity Search
* Retrieval-Augmented Generation

### Frameworks

* LangChain
* LangGraph

### LLM Platforms / Models

* OpenAI
* Google Gemini
* Anthropic
* Groq
* Ollama
* Llama 3.2

### Application Development

* Streamlit

### Data & Tools

* SQLite
* SQL
* Pydantic
* Chroma
* PyPDF
* BeautifulSoup
* Wikipedia

---

# Learning Progress

This repository is continuously updated as I build and experiment with new Generative AI applications.

Current areas of hands-on learning include:

* Python for Generative AI
* LLM APIs
* LangChain
* Retrieval-Augmented Generation
* Agentic RAG
* AI Agents
* LangGraph
* Structured data validation
* AI + SQL applications
* Streamlit GenAI applications

---

# Repository Structure

```text
Generative-ai-projects/
|
+-- apps/
|   +-- 1_QNA_bot.py
|   +-- 2_google_agents.py
|   +-- 3_qna_bot_with_groq.py
|   +-- 4_sql_agent.py
|   +-- 5_rag_agent.py
|
+-- notebooks/
|   +-- 12_vector_embeddings.ipynb
|   +-- 13_rag_based_pdf_qna_bot.ipynb
|   +-- 14_rag_ai_agent.ipynb
|   +-- 15_pydantic_data_validation.ipynb
|   +-- 16_basic_langgraph.ipynb
|
+-- data/
+-- certs/
+-- requirements.txt
+-- README.md
```

---

# How to Run

Clone the repository:

```bash
git clone https://github.com/manishsachan069-cyber/Generative-ai-projects.git
```

Move into the project directory:

```bash
cd Generative-ai-projects
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add the API keys required by the specific application.

Some projects use external LLM APIs, while the SQL Agent uses **Ollama** for local LLM execution.

---

# Career Goal

I am currently building my skills toward a career in **Generative AI Development**, with a focus on developing practical LLM-powered applications, RAG systems, AI agents, and agentic workflows.

This repository will continue to evolve as I build more advanced projects and deepen my understanding of Generative AI.
