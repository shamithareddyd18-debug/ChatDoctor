VECTOR_DB = []

def add_document(
    embedding,
    text
):

    VECTOR_DB.append(
        {
            "embedding": embedding,
            "text": text
        }
    )
