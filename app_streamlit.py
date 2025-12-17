"""Application Streamlit - Dashboard Open Data."""
import streamlit as st
import pandas as pd
from pathlib import Path

# Import des modules locaux
from utils.data import load_data, filter_data, get_data_summary
from utils.charts import (
    create_bar_chart, create_pie_chart, 
    create_scatter_plot, create_histogram,
    create_heatmap
)
from utils.chatbot import DataChatbot

# Configuration de la page
st.set_page_config(
    page_title="Chocolat Explorer",
    page_icon="🍫",
    layout="wide"
)

# --- Chargement des données ---
@st.cache_data
def get_data():
    """Charge les données avec cache."""
    data_path = Path("data/processed")
    parquet_files = list(data_path.glob("*.parquet"))
    
    if not parquet_files:
        st.error("Aucun fichier Parquet trouvé dans data/processed/")
        st.stop()
    
    return load_data(parquet_files[0])

df = get_data()

# --- Header ---
st.title("🍫 Chocolat Data Explorer")
st.markdown("*Explorez les données de produits chocolatés de manière interactive*")

# --- Sidebar : Filtres ---
st.sidebar.header("🔍 Filtres")

# Filtre par marque
if 'brands' in df.columns:
    brands_list = df['brands'].dropna().unique().tolist()
    if brands_list:
        selected_brands = st.sidebar.multiselect(
            "Filtrer par marque",
            options=brands_list,
            default=[]
        )
        if selected_brands:
            df = df[df['brands'].isin(selected_brands)]

# Filtre par Nutriscore
if 'nutriscore_grade' in df.columns:
    nutriscore_list = df['nutriscore_grade'].dropna().unique().tolist()
    if nutriscore_list:
        selected_nutriscore = st.sidebar.multiselect(
            "Filtrer par Nutriscore",
            options=sorted(nutriscore_list),
            default=[]
        )
        if selected_nutriscore:
            df = df[df['nutriscore_grade'].isin(selected_nutriscore)]

# Filtre par ville
if 'city' in df.columns:
    cities_list = df['city'].dropna().unique().tolist()
    if cities_list and len(cities_list) <= 50:
        selected_cities = st.sidebar.multiselect(
            "Filtrer par ville",
            options=sorted(cities_list),
            default=[]
        )
        if selected_cities:
            df = df[df['city'].isin(selected_cities)]

# --- Métriques ---
st.header("📈 Vue d'ensemble")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total produits", f"{len(df)}")
with col2:
    st.metric("Colonnes", len(df.columns))
with col3:
    if 'brands' in df.columns:
        unique_brands = df['brands'].nunique()
        st.metric("Marques uniques", unique_brands)
with col4:
    if 'city' in df.columns:
        unique_cities = df['city'].nunique()
        st.metric("Villes", unique_cities)

# --- Visualisations ---
st.header("📊 Visualisations")

# Tabs pour différentes visualisations
tab1, tab2, tab3, tab4 = st.tabs(["📊 Marques", "🎯 Nutrition", "🗺️ Géographie", "🔥 Corrélations"])

with tab1:
    st.subheader("Distribution des produits par marque")
    if 'brands' in df.columns:
        brand_counts = df['brands'].value_counts().head(10).reset_index()
        brand_counts.columns = ['brands', 'count']
        fig = create_bar_chart(
            brand_counts,
            x='brands',
            y='count',
            title='Top 10 des marques'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Colonne 'brands' non disponible")

with tab2:
    st.subheader("Analyse nutritionnelle")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Histogramme des sucres
        if 'sugars_100g' in df.columns:
            fig = create_histogram(
                df,
                x='sugars_100g',
                title='Distribution des sucres (g/100g)'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Histogramme des graisses
        if 'fat_100g' in df.columns:
            fig = create_histogram(
                df,
                x='fat_100g',
                title='Distribution des graisses (g/100g)'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Scatter plot Sucres vs Graisses
    if 'sugars_100g' in df.columns and 'fat_100g' in df.columns:
        color_col = 'nutriscore_grade' if 'nutriscore_grade' in df.columns else None
        fig = create_scatter_plot(
            df,
            x='sugars_100g',
            y='fat_100g',
            color=color_col,
            title='Sucres vs Graisses'
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Distribution géographique")
    
    if 'city' in df.columns:
        city_counts = df['city'].value_counts().head(10).reset_index()
        city_counts.columns = ['city', 'count']
        fig = create_bar_chart(
            city_counts,
            x='city',
            y='count',
            title='Top 10 des villes'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Carte si latitude/longitude disponibles
    if 'latitude' in df.columns and 'longitude' in df.columns:
        df_map = df[['latitude', 'longitude']].dropna()
        if len(df_map) > 0:
            st.map(df_map)

with tab4:
    st.subheader("Matrice de corrélation")
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 1:
        fig = create_heatmap(df, title='Corrélations entre variables numériques')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Pas assez de colonnes numériques pour une matrice de corrélation")

# --- Données brutes ---
st.header("📋 Données brutes")
st.dataframe(df, use_container_width=True)
# --- Export des données ---
st.header("📥 Export des données")

col1, col2, col3 = st.columns(3)

with col1:
    # Export CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📄 Télécharger CSV",
        data=csv,
        file_name=f"chocolats_export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True
    )

with col2:
    # Export Excel
    from io import BytesIO
    
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Données', index=False)
        
        # Ajouter une feuille avec les statistiques
        if len(df.select_dtypes(include=['number']).columns) > 0:
            stats = df.describe()
            stats.to_excel(writer, sheet_name='Statistiques')
    
    buffer.seek(0)
    
    st.download_button(
        label="📊 Télécharger Excel",
        data=buffer,
        file_name=f"chocolats_export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

with col3:
    # Export JSON
    json_data = df.to_json(orient='records', indent=2)
    st.download_button(
        label="📋 Télécharger JSON",
        data=json_data,
        file_name=f"chocolats_export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json",
        use_container_width=True
    )

# Afficher un résumé de l'export
st.info(f"💡 **{len(df)} lignes** seront exportées (filtres appliqués)")
# --- Chatbot ---
st.header("🤖 Assistant Data")

# Initialiser le chatbot (avec cache de session)
if "chatbot" not in st.session_state:
    st.session_state.chatbot = DataChatbot(df, model="ollama/llama2")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l'historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input utilisateur
if prompt := st.chat_input("Posez une question sur les données..."):
    # Afficher le message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Obtenir la réponse
    with st.chat_message("assistant"):
        with st.spinner("Réflexion..."):
            response = st.session_state.chatbot.chat(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Bouton pour réinitialiser
if st.button("🔄 Nouvelle conversation"):
    st.session_state.chatbot.reset()
    st.session_state.messages = []
    st.rerun()