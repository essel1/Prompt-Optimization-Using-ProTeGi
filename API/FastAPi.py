from fastapi import FastAPI, Query, Request
from typing import List
import random

app = FastAPI()

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message":"API is up and running"}

# Endpoint for a prompt optimization example
@app.post("/optimize-prompt/")
async def optimize_prompt(prompts: List[str] = Query(..., description="List of prompts")):
    # Placeholder logic: Simulate a response for each prompt
    responses = [f"Optimized version of '{prompt}':'{prompt} improved'" for prompt in prompts]
    return {"optimized_prompts":responses}

