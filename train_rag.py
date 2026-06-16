from ChatDoctor_RAG.chunk_documents import chunk_documents
from ChatDoctor_RAG.create_embeddings import create_embedding
from ChatDoctor_RAG.vector_database import add_document

document = """
Diabetes is a chronic disease
that affects blood sugar levels.
"""

chunks = chunk_documents(document)

for chunk in chunks:

    embedding = create_embedding(
        chunk
    )

    add_document(
        embedding,
        chunk
    )

print(
    "Knowledge Base Created"
)
