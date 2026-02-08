from fastapi import FastAPI
from pydantic import BaseModel
from agent import LLMAgent

app = FastAPI()
agent = LLMAgent("./models/gpt2-networking")

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def generate_text(prompt: Prompt):
    response = agent.generate(prompt.text)
    return {"response": response}
