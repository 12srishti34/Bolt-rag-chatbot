import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from app.db import SessionLocal
from app.models.models import DocumentChunk
import uuid

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

db = SessionLocal()

with open("documents/bolt_test.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunk_id = str(uuid.uuid4())

embedding = model.encode(text).tolist()

# Upload to Pinecone
index.upsert(
    vectors=[
        {
            "id": chunk_id,
            "values": embedding,
            "metadata": {
                "source": "bolt_test.txt"
            }
        }
    ]
)

# Save in PostgreSQL
doc = DocumentChunk(
    id=chunk_id,
    source="bolt_test.txt",
    text=text,
    page_number=1
)

db.add(doc)
db.commit()

db.close()

print("Document uploaded successfully!")