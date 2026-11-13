# RAG Question Answer System

A FastAPI-based Retrieval-Augmented Generation (RAG) question-answering application that retrieves relevant information from pre-loaded documents and generates AI-powered responses.

> **Project Context:** This project was provided as part of an interview assignment. The existing starter code was used as the foundation. My involvement focused on setting up the project locally, troubleshooting issues, and getting the application running with AI-assisted guidance. This is not an application developed entirely from scratch by me.

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Vector Database:** Pinecone
- **AI Model:** Groq (Llama)
- **Embeddings:** Sentence Transformers
- **Frontend:** HTML, CSS, JavaScript

## Project Overview

The application uses the RAG approach to answer questions using information retrieved from pre-loaded business documents.

The general workflow involves:

1. Processing and ingesting documents.
2. Generating embeddings for document content.
3. Storing vector representations in Pinecone.
4. Retrieving relevant information when a question is submitted.
5. Generating a response using the Groq language model.

## Prerequisites

Before running the application, you will need:

- Python 3.8 or higher
- PostgreSQL
- A Pinecone account and API key
- A Groq account and API key

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/12srishti34/Bolt-rag-chatbot.git
cd Bolt-rag-chatbot
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Use `.env.example` as a reference and configure the required variables:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/your_database_name

PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_index_name

GROQ_API_KEY=your_groq_api_key

UPLOAD_DIR=app/uploads
```

**Important:** Never upload your actual `.env` file, API keys, passwords, or other secrets to GitHub.

### 5. Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE your_database_name;
```

Run database migrations:

```bash
alembic upgrade head
```

### 6. Pinecone Configuration

1. Create an account at [Pinecone](https://www.pinecone.io/).
2. Create a vector index.
3. Configure the index according to the embedding model used by the application.
4. Add the index name and API key to your `.env` file.

### 7. Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open the application at:

- **Local:** http://localhost:8000

FastAPI documentation may be available at:

- http://localhost:8000/docs

## API Endpoints

The existing project README documents the following endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/test-pinecone/` | Test Pinecone connection |
| POST | `/ask-question/` | Submit a question |

Example request:

```json
{
  "question": "Your question here"
}
```

## Project Structure

```text
Bolt-rag-chatbot/
│
├── alembic/                 # Database migrations
├── app/
│   ├── models/              # Database models
│   └── db.py                # Database configuration
│
├── documents/               # Document files
├── static/                  # Static assets
├── templates/               # HTML templates
│
├── main.py                  # FastAPI application
├── ingest.py                # Document ingestion
├── requirements.txt         # Python dependencies
├── alembic.ini              # Alembic configuration
├── Dockerfile
├── docker-compose.prod.yml
├── .env.example             # Environment variable template
└── README.md
```

## My Involvement

- Worked with an existing Python/FastAPI RAG project supplied as an interview assignment.
- Set up the project in a local development environment.
- Worked through setup and runtime issues to get the application running.
- Used ChatGPT-assisted guidance for troubleshooting and understanding the existing codebase.

**Note:** The original application and starter code were not created from scratch by me. The repository is shared for learning and portfolio documentation purposes.

## AI Assistance

ChatGPT was used as a supporting tool for technical guidance, debugging, and troubleshooting during the setup process.

