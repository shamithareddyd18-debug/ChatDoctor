from medical_rag.retrieval import retrieve

def retrieve_context(query):

    documents = retrieve(query)

    return "\n".join(documents)
