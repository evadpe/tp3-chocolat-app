"""Module chatbot pour interroger les données."""
import pandas as pd
from litellm import completion
from dotenv import load_dotenv
import json
import os

load_dotenv()

# Pour Streamlit Cloud, utiliser st.secrets si disponible
try:
    import streamlit as st
    if hasattr(st, 'secrets'):
        os.environ['GROQ_API_KEY'] = st.secrets.get('GROQ_API_KEY', '')
except:
    pass


class DataChatbot:
    """Chatbot pour interroger les données en langage naturel."""  
    def __init__(self, df: pd.DataFrame, model: str = "gemini/gemini-2.0-flash-exp"):
        self.df = df
        self.model = model
        self.context = self._build_context()
        self.history = []
    
    def _build_context(self) -> str:
        """Construit le contexte des données pour l'IA."""
        sample = self.df.head(5).to_string()
        stats = self.df.describe().to_string()
        
        return f"""
Tu es un assistant data qui aide à analyser un dataset de produits alimentaires.

STRUCTURE DU DATASET :
- Colonnes : {list(self.df.columns)}
- Types : {self.df.dtypes.to_dict()}
- Nombre de lignes : {len(self.df)}

ÉCHANTILLON :
{sample}

STATISTIQUES :
{stats}

Tu peux :
1. Répondre à des questions sur les données
2. Proposer des analyses
3. Générer du code Python pour manipuler les données
4. Expliquer les tendances observées

Sois concis et précis dans tes réponses.
"""
    
    def chat(self, user_message: str) -> str:
        """
        Envoie un message au chatbot et retourne la réponse.
        
        Args:
            user_message: Question de l'utilisateur
        
        Returns:
            Réponse du chatbot
        """
        # Ajouter le contexte au premier message
        messages = [
            {"role": "system", "content": self.context}
        ]
        
        # Ajouter l'historique
        messages.extend(self.history)
        
        # Ajouter le nouveau message
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = completion(
                model=self.model,
                messages=messages
            )
            
            assistant_message = response.choices[0].message.content
            
            # Mettre à jour l'historique
            self.history.append({"role": "user", "content": user_message})
            self.history.append({"role": "assistant", "content": assistant_message})
            
            # Limiter l'historique à 10 échanges
            if len(self.history) > 20:
                self.history = self.history[-20:]
            
            return assistant_message
            
        except Exception as e:
            return f"Erreur : {str(e)}"
    
    def reset(self):
        """Réinitialise l'historique de conversation."""
        self.history = []