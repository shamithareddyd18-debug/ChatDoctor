chat_history = []

def save_chat(question, answer):

    chat_history.append({
        "question": question,
        "answer": answer
    })


def get_history():

    return chat_history


def clear_history():

    chat_history.clear()
