from vector_database import (
    search_vector_db
)

def retrieve(query):

    documents = search_vector_db(
        query
    )

    return documents
