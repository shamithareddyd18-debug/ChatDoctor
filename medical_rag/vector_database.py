VECTOR_DATABASE = []

def add_document(
    embedding,
    text
):

    VECTOR_DATABASE.append(
        {
            "embedding": embedding,
            "text": text
        }
    )

def search_vector_db(
    query
):

    results = []

    for item in VECTOR_DATABASE:

        results.append(
            item["text"]
        )

    return results[:3]
