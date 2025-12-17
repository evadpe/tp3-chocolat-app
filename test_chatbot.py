"""Test du chatbot."""
from utils.data import load_data
from utils.chatbot import DataChatbot
from pathlib import Path

# Charger les données
data_path = Path("data/processed")
parquet_files = list(data_path.glob("*.parquet"))

if parquet_files:
    print(f"✅ Chargement des données...")
    df = load_data(parquet_files[0])
    
    print(f"✅ Initialisation du chatbot avec Ollama...")
    # Utiliser Ollama (local, gratuit, aucune limite)
    chatbot = DataChatbot(df, model="ollama/llama2")
    
    print("\n🤖 Test du chatbot :")
    print("=" * 50)
    
    # Question test
    question = "Quelles sont les principales informations sur ce dataset ?"
    print(f"\n👤 Question : {question}")
    
    response = chatbot.chat(question)
    print(f"\n🤖 Réponse : {response}")
    
else:
    print("❌ Aucun fichier Parquet trouvé")