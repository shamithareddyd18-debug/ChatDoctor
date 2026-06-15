from fastapi import FastAPI
from chatdoctor_api.chat import generate_response

app = FastAPI(title="ChatDoctor")

@app.get("/")
def home():
    return {"message": "ChatDoctor Running"}

@app.post("/chat")
def chat(data: dict):

    response = generate_response(
        data["message"],
        role=data.get("role", "general")
    )

    return {
        "response": response
    }
