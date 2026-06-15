from chatdoctor_api.rag import retrieve_context

def generate_response(
    query: str,
    role: str
):

    context = retrieve_context(query)

    if role == "doctor":

        return (
            f"[Doctor Mode]\n"
            f"Context: {context}\n"
            f"Query: {query}"
        )

    return (
        f"[Patient Mode]\n"
        f"{query}"
    )
