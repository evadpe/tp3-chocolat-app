"""Créer un fichier de données exemple pour le déploiement."""
import pandas as pd
from pathlib import Path

# Charger tes données complètes
df = pd.read_parquet("data/processed/products_chocolats_clean_20251216_163506.parquet")

# Créer un sample (toutes les données dans ton cas)
df_sample = df.copy()

# Sauvegarder
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)
df_sample.to_parquet(output_dir / "sample_data.parquet", index=False)

print(f"✅ Fichier sample créé : {len(df_sample)} lignes")