from medical_rag.retrieval import retrieve

def retrieve_context(
    query
):

    docs = retrieve(query)

    return "\n".join(docs)
