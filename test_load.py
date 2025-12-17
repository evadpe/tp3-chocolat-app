"""Test rapide du chargement des données."""
from utils.data import load_data
from utils.charts import create_bar_chart
from pathlib import Path

# Trouver le fichier parquet
data_path = Path("data/processed")
parquet_files = list(data_path.glob("*.parquet"))

if parquet_files:
    print(f"✅ Fichier trouvé : {parquet_files[0]}")
    df = load_data(parquet_files[0])
    print(f"✅ Données chargées : {len(df)} lignes, {len(df.columns)} colonnes")
    print(f"✅ Colonnes : {list(df.columns)}")
    
    # Tester un graphique simple
    print("\n📊 Test de visualisation...")
    # Créer un bar chart du nombre de produits par marque
    brand_counts = df['brands'].value_counts().reset_index()
    brand_counts.columns = ['brands', 'count']
    
    fig = create_bar_chart(
        brand_counts,
        x='brands',
        y='count',
        title='Nombre de produits par marque'
    )
    print("✅ Graphique créé avec succès !")
else:
    print("❌ Aucun fichier Parquet trouvé dans data/processed/")