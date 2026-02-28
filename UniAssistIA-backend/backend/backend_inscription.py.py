# backend_inscription.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/api/ai-inscription")
async def answer_inscription(question: Question):
    q = question.question.lower()
    if "documents" in q or "quoi fournir" in q:
        answer = "Pour l'inscription, fournissez : formulaire rempli, copie de la carte d'identité, relevé de notes, photo récente et justificatif de paiement."
    elif "comment m'inscrire" in q or "en ligne" in q:
        answer = "Pour vous inscrire en ligne : 1) Créez un compte, 2) Remplissez le formulaire, 3) Téléversez vos documents, 4) Soumettez et recevez confirmation par email."
    else:
        answer = "Je peux vous guider sur l'inscription. Posez une question sur documents, procédure ou suivi de votre dossier."
    
    return {"answer": answer}