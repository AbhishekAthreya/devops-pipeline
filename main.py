from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    "Talk is cheap. Show me the code.",
    "Programs must be written for people to read.",
    "First, solve the problem. Then, write the code."
]

@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}
