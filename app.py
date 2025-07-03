from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional

class ChatRequest(BaseModel):
    message: str
    language: str = "it"
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    language: str
    sources: List[Dict]
    category: Optional[str]
    confidence: float

app = FastAPI(
    title="JOKKO AI",
    description="Chatbot per migranti africani in Italia",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "Benvenuto in JOKKO AI"}

@app.get("/api/health")
def health():
    return {"status": "ok", "message": "JOKKO è attivo!"}

@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    msg = req.message.lower()
    lang = req.language

    if "permesso" in msg:
        response = "Devi andare in Questura con passaporto, foto tessera e marca da bollo da 16€."
        category = "permesso_soggiorno"
    else:
        response = "Ciao! Sono JOKKO AI. Posso aiutarti su permesso di soggiorno, lavoro, casa, sanità e diritti."
        category = "generale"

    return ChatResponse(
        response=response,
        language=lang,
        sources=[{"title": "Ministero dell'Interno", "url": "https://www.interno.gov.it"}],
        category=category,
        confidence=0.9
    )
