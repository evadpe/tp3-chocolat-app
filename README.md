# TP3 - Application Data Interactive avec Chatbot 🍫

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tp3-chocolat-app-czizcht93pjkxws6ftiyuc.streamlit.app)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

> Application web interactive d'analyse de données de produits chocolatés avec chatbot IA intégré.

## 🌐 Application en ligne

**👉 [Accéder à l'application déployée](https://tp3-chocolat-app-czizcht93pjkxws6ftiyuc.streamlit.app)**

---

## 📋 Table des matières

- [Objectifs](#-objectifs)
- [Fonctionnalités](#-fonctionnalités)
- [Technologies utilisées](#-technologies-utilisées)
- [Installation locale](#-installation-locale)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [Bonus implémentés](#-bonus-implémentés)
- [Captures d'écran](#-captures-décran)
- [Évaluation](#-évaluation)
- [Auteur](#-auteur)

---

## 🎯 Objectifs

Ce projet est une application web interactive construite avec **Streamlit** qui permet :

1. ✅ Créer des visualisations interactives avec Plotly
2. ✅ Construire une application data avec Streamlit
3. ✅ Intégrer un chatbot LLM pour interroger les données
4. ✅ Déployer une application fonctionnelle sur le cloud

---

## ✨ Fonctionnalités

### 📊 Visualisations interactives
- **Graphiques Plotly** : Bar charts, pie charts, scatter plots, histogrammes, heatmaps
- **4 onglets thématiques** :
  - 📊 Distribution par marques
  - 🎯 Analyse nutritionnelle (sucres, graisses, nutriscore)
  - 🗺️ Distribution géographique avec carte interactive
  - 🔥 Matrice de corrélations

### 🔍 Filtres dynamiques
- Filtrage par **marque**
- Filtrage par **Nutriscore**
- Filtrage par **ville**
- Mise à jour en temps réel des visualisations

### 📈 Métriques clés
- Total de produits
- Nombre de colonnes
- Marques uniques
- Villes représentées

### 🤖 Chatbot IA
- Assistant intelligent alimenté par **Groq (Llama 3.1)**
- Répond aux questions sur les données en langage naturel
- Historique de conversation
- Capacité d'analyse et de recommandations

### 📥 Export de données
- Export **CSV** des données filtrées
- Export **Excel** avec feuille de statistiques
- Export **JSON**
- Horodatage automatique des fichiers

### 🎨 Interface personnalisée
- Thème chocolat sur mesure
- Design professionnel et épuré
- Navigation intuitive

---

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| **Streamlit** | Framework d'application web |
| **Plotly** | Visualisations interactives |
| **Pandas** | Manipulation de données |
| **DuckDB** | Chargement optimisé des données |
| **LiteLLM** | Interface unifiée pour les LLMs |
| **Groq** | API LLM (déploiement cloud) |
| **Ollama** | LLM local (développement) |
| **Openpyxl** | Export Excel |

---

## 💻 Installation locale

### Prérequis
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (gestionnaire de packages)
- [Ollama](https://ollama.com/) (pour le chatbot local)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/evadpe/tp3-chocolat-app.git
cd tp3-chocolat-app
```

2. **Installer les dépendances**
```bash
uv add streamlit plotly pandas duckdb litellm python-dotenv openpyxl
```

3. **Installer Ollama et télécharger le modèle**
```bash
# Installer Ollama depuis https://ollama.com/
ollama pull llama2
```

4. **Créer le fichier .env** (optionnel pour le cloud)
```env
GROQ_API_KEY=votre_clé_groq
```

5. **Lancer l'application**
```bash
uv run streamlit run app_streamlit.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

---

## 🚀 Utilisation

### En local
```bash
uv run streamlit run app_streamlit.py
```

### En ligne
Accédez directement à : **https://tp3-chocolat-app-czizcht93pjkxws6ftiyuc.streamlit.app**

### Fonctionnalités principales

1. **Explorer les données**
   - Utilisez les filtres dans la sidebar
   - Naviguez entre les différents onglets de visualisation
   - Consultez les métriques en temps réel

2. **Visualiser**
   - Interagissez avec les graphiques Plotly (zoom, hover, export)
   - Explorez la carte géographique
   - Analysez les corrélations

3. **Interroger avec le chatbot**
   - Posez des questions en langage naturel
   - Demandez des analyses ou recommandations
   - Réinitialisez la conversation si nécessaire

4. **Exporter les données**
   - Appliquez vos filtres
   - Choisissez le format (CSV, Excel, JSON)
   - Téléchargez instantanément

---

## 📁 Structure du projet

```
tp3-chocolat-app/
├── .streamlit/
│   ├── config.toml              # Configuration du thème
│   └── secrets.toml             # Clés API (non versionné)
├── data/
│   └── processed/
│       └── sample_data.parquet  # Données de produits chocolatés
├── utils/
│   ├── __init__.py
│   ├── data.py                  # Chargement et filtrage des données
│   ├── charts.py                # Visualisations Plotly
│   └── chatbot.py               # Assistant IA avec LiteLLM
├── app_streamlit.py             # Application principale
├── requirements.txt             # Dépendances pour le déploiement
├── .gitignore
└── README.md
```

---

## 🎁 Bonus implémentés

| Bonus | Points | Statut |
|-------|--------|--------|
| **Déploiement sur Streamlit Cloud** | +2 | ✅ Implémenté |
| **Thème personnalisé** | +1 | ✅ Implémenté |
| **Export des données filtrées (CSV/Excel/JSON)** | +1 | ✅ Implémenté |
| **Total bonus** | +4 | ✅ |

---

## 📸 Captures d'écran

### Vue d'ensemble
![Vue d'ensemble](https://via.placeholder.com/800x400/FFF8DC/2C1810?text=Dashboard+Principal)

### Visualisations
![Visualisations](https://via.placeholder.com/800x400/FFF8DC/2C1810?text=Graphiques+Interactifs)

### Chatbot IA
![Chatbot](https://via.placeholder.com/800x400/FFF8DC/2C1810?text=Assistant+IA)

---

## 📊 Évaluation

| Critère | Points | Auto-évaluation |
|---------|--------|-----------------|
| **Application fonctionnelle** | /4 | ✅ Lancement sans erreur, navigation fluide |
| **Visualisations** | /3 | ✅ 6 types de graphiques interactifs (bar, pie, scatter, histogram, heatmap, map) |
| **Filtres** | /2 | ✅ Filtres dynamiques par marque, nutriscore, ville |
| **Chatbot** | /4 | ✅ Répond correctement avec Groq/Ollama |
| **Qualité du code** | /2 | ✅ Organisation modulaire, commentaires, docstrings |
| **Bonus** | +4 | ✅ Déploiement (+2), Thème (+1), Export (+1) |
| **Total** | **/19** | **19/15** |

---

## 🔧 Configuration

### Thème personnalisé
Le thème "Chocolat" est défini dans `.streamlit/config.toml` :
```toml
[theme]
primaryColor = "#8B4513"           # Marron chocolat
backgroundColor = "#FFF8DC"         # Beige crème
secondaryBackgroundColor = "#F5DEB3" # Blé doré
textColor = "#2C1810"              # Marron foncé
```

### Chatbot
- **Local** : Ollama avec Llama 2
- **Cloud** : Groq avec Llama 3.1 70B

---

## 👩‍💻 Auteur

**Eva DEPAEPE**  
Mastère Data Engineering - SEENOVATE  
Décembre 2024

---

## 📝 Licence

Ce projet est réalisé dans le cadre du TP3 du cours Open Data.

---

## 🙏 Remerciements

- [Streamlit](https://streamlit.io/) pour le framework
- [Plotly](https://plotly.com/) pour les visualisations
- [Groq](https://groq.com/) pour l'API LLM gratuite
- [Ollama](https://ollama.com/) pour l'inférence locale
- [OpenFoodFacts](https://world.openfoodfacts.org/) pour les données

---
