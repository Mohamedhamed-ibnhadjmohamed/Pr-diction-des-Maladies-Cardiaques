import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier

# Configuration de la page
st.set_page_config(
    page_title="Prédiction des Maladies Cardiaques",
    page_icon=" heart: ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre et description
st.title(" heart: Prédiction des Maladies Cardiaques")
st.markdown("""
Cette application utilise des algorithmes de Machine Learning pour prédire le risque de maladies cardiaques 
basé sur les données cliniques du patient.
""")

# Sidebar pour la sélection du modèle
st.sidebar.header("Configuration du Modèle")
model_choice = st.sidebar.selectbox(
    "Choisissez un modèle de prédiction:",
    ["Random Forest", "AdaBoost", "Gradient Boosting", "SVM", "Decision Tree", 
     "KNN", "GaussianNB", "Régression Logistique", "ExtraTrees"]
)

# Chargement des données et entraînement des modèles
@st.cache_data
def load_data():
    df = pd.read_csv("data/heart_disease_dataset1.csv")
    return df

@st.cache_resource
def train_models():
    df = load_data()
    X = df.drop("target", axis=1)
    y = df.target
    
    # Définition des modèles avec leurs meilleurs paramètres
    models = {
        "Random Forest": RandomForestClassifier(n_estimators=510, min_samples_split=18, min_samples_leaf=19, max_depth=5, random_state=42),
        "AdaBoost": AdaBoostClassifier(n_estimators=50, learning_rate=0.1, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(n_estimators=50, min_samples_split=10, min_samples_leaf=4, max_depth=3, learning_rate=0.01, random_state=42),
        "SVM": SVC(kernel='poly', C=100, probability=True, random_state=42),
        "Decision Tree": DecisionTreeClassifier(min_samples_split=18, min_samples_leaf=9, max_depth=5, random_state=42),
        "KNN": KNeighborsClassifier(weights="distance", n_neighbors=15, algorithm="auto"),
        "GaussianNB": GaussianNB(),
        "Régression Logistique": LogisticRegression(C=4.281332398719396, solver="liblinear", random_state=42),
        "ExtraTrees": ExtraTreesClassifier(n_estimators=700, min_samples_split=2, min_samples_leaf=1, max_features='sqrt', max_depth=80, bootstrap=False, random_state=42)
    }
    
    # Entraînement de tous les modèles
    trained_models = {}
    for name, model in models.items():
        model.fit(X, y)
        trained_models[name] = model
    
    return trained_models, X.columns.tolist()

# Charger les modèles
models, feature_names = train_models()

# Formulaire de saisie des données patient
st.header(" Saisie des Données Patient")

col1, col2 = st.columns(2)

with col1:
    # Âge
    age = st.number_input("Âge", min_value=1, max_value=120, value=50, help="Âge du patient en années")
    
    # Genre
    gender = st.selectbox("Genre", ["Homme", "Femme"], help="Genre du patient")
    gender_encoded = 1 if gender == "Homme" else 0
    
    # Cholestérol
    cholesterol = st.number_input("Cholestérol (mg/dL)", min_value=100, max_value=400, value=200, help="Niveau de cholestérol")
    
    # Pression artérielle
    blood_pressure = st.number_input("Pression Artérielle (mmHg)", min_value=80, max_value=200, value=120, help="Pression artérielle systolique")
    
    # Fréquence cardiaque
    heart_rate = st.number_input("Fréquence Cardiaque (bpm)", min_value=40, max_value=200, value=70, help="Fréquence cardiaque au repos")

with col2:
    # Tabagisme
    smoking = st.selectbox("Tabagisme", ["Jamais", "Ancien fumeur", "Fumeur actuel"], help="Statut tabagique")
    smoking_encoded = {"Jamais": 0, "Ancien fumeur": 1, "Fumeur actuel": 2}[smoking]
    
    # Consommation d'alcool
    alcohol = st.selectbox("Consommation d'Alcool", ["Aucune", "Légère", "Modérée", "Élevée"], help="Niveau de consommation d'alcool")
    alcohol_encoded = {"Aucune": 0, "Légère": 1, "Modérée": 2, "Élevée": 3}[alcohol]
    
    # Heures d'exercice
    exercise_hours = st.number_input("Heures d'Exercice par semaine", min_value=0, max_value=20, value=3, help="Nombre d'heures d'exercice physique par semaine")
    
    # Antécédents familiaux
    family_history = st.selectbox("Antécédents Familiaux", ["Non", "Oui"], help="Antécédents de maladies cardiaques dans la famille")
    family_history_encoded = 1 if family_history == "Oui" else 0

col3, col4 = st.columns(2)

with col3:
    # Diabète
    diabetes = st.selectbox("Diabète", ["Non", "Oui"], help="Le patient est-il diabétique?")
    diabetes_encoded = 1 if diabetes == "Oui" else 0
    
    # Obésité
    obesity = st.selectbox("Obésité", ["Non", "Oui"], help="Le patient est-il considéré comme obèse?")
    obesity_encoded = 1 if obesity == "Oui" else 0
    
    # Niveau de stress
    stress_level = st.slider("Niveau de Stress (1-10)", min_value=1, max_value=10, value=5, help="Niveau de stress perçu")

with col4:
    # Taux de sucre dans le sang
    blood_sugar = st.number_input("Taux de Sucre dans le Sang (mg/dL)", min_value=50, max_value=300, value=100, help="Taux de glucose sanguin")
    
    # Angine induite par l'exercice
    exercise_induced_angina = st.selectbox("Angine Induite par l'Exercice", ["Non", "Oui"], help="Douleur thoracique lors de l'exercice")
    angina_encoded = 1 if exercise_induced_angina == "Oui" else 0
    
    # Type de douleur thoracique
    chest_pain_type = st.selectbox(
        "Type de Douleur Thoracique", 
        ["Aucune", "Angine typique", "Angine atypique", "Douleur non angineuse", "Asymptomatique"],
        help="Type de douleur thoracique ressentie"
    )
    chest_pain_encoded = ["Aucune", "Angine typique", "Angine atypique", "Douleur non angineuse", "Asymptomatique"].index(chest_pain_type)

# Création du dataframe pour la prédiction
patient_data = pd.DataFrame({
    'age': [age],
    'gender': [gender_encoded],
    'chol': [cholesterol],
    'bp': [blood_pressure],
    'hr': [heart_rate],
    'smoke': [smoking_encoded],
    'alcohol': [alcohol_encoded],
    'exercise': [exercise_hours],
    'family_hist': [family_history_encoded],
    'diabetes': [diabetes_encoded],
    'obesity': [obesity_encoded],
    'stress': [stress_level],
    'sugar': [blood_sugar],
    'angina': [angina_encoded],
    'cp': [chest_pain_encoded]
})

# Bouton de prédiction
if st.button(" Lancer la Prédiction", type="primary"):
    # Sélection du modèle
    model = models[model_choice]
    
    # Prédiction
    prediction = model.predict(patient_data)[0]
    prediction_proba = model.predict_proba(patient_data)[0]
    
    # Affichage des résultats
    st.header(" Résultats de la Prédiction")
    
    col_result1, col_result2 = st.columns(2)
    
    with col_result1:
        if prediction == 1:
            st.error(" heart: **Risque Élevé de Maladie Cardiaque**")
            st.markdown("**Recommandation:** Consultation médicale urgente recommandée")
        else:
            st.success(" heart: **Faible Risque de Maladie Cardiaque**")
            st.markdown("**Recommandation:** Maintenir un mode de vie sain")
    
    with col_result2:
        # Probabilités
        prob_no_disease = prediction_proba[0] * 100
        prob_disease = prediction_proba[1] * 100
        
        fig, ax = plt.subplots(figsize=(8, 6))
        labels = ['Sain', 'Malade']
        sizes = [prob_no_disease, prob_disease]
        colors = ['lightgreen', 'lightcoral']
        
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'Probabilités - {model_choice}', fontsize=14, fontweight='bold')
        
        st.pyplot(fig)
    
    # Détails des probabilités
    st.subheader("Détails des Probabilités")
    col_prob1, col_prob2 = st.columns(2)
    
    with col_prob1:
        st.metric("Probabilité d'être Sain", f"{prob_no_disease:.1f}%", delta=None)
    
    with col_prob2:
        st.metric("Probabilité de Maladie Cardiaque", f"{prob_disease:.1f}%", delta=None)

# Section d'information
st.header("Informations sur les Modèles")

# Performances des modèles
performance_data = {
    "Modèle": ["Decision Tree", "AdaBoost", "Gradient Boosting", "Random Forest", "ExtraTrees", 
               "SVM", "KNN", "GaussianNB", "Régression Logistique"],
    "Accuracy": [100.0, 100.0, 100.0, 99.5, 96.5, 94.0, 93.5, 92.0, 88.5],
    "Precision": [100.0, 100.0, 100.0, 100.0, 100.0, 92.3, 93.3, 95.6, 86.7],
    "Recall": [100.0, 100.0, 100.0, 98.7, 91.0, 92.3, 89.7, 83.3, 83.3],
    "F1-Score": [100.0, 100.0, 100.0, 99.4, 95.3, 92.3, 91.5, 89.0, 85.0]
}

perf_df = pd.DataFrame(performance_data)

# Affichage du tableau des performances
st.subheader("Performances des Modèles")
st.dataframe(perf_df, use_container_width=True)

# Visualisation des performances
st.subheader("Comparaison des Performances")

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Performances des Différents Modèles', fontsize=16, fontweight='bold')

# Accuracy
axes[0, 0].barh(perf_df['Modèle'], perf_df['Accuracy'], color='skyblue')
axes[0, 0].set_title('Accuracy (%)')
axes[0, 0].set_xlim(80, 105)

# Precision
axes[0, 1].barh(perf_df['Modèle'], perf_df['Precision'], color='lightgreen')
axes[0, 1].set_title('Precision (%)')
axes[0, 1].set_xlim(80, 105)

# Recall
axes[1, 0].barh(perf_df['Modèle'], perf_df['Recall'], color='orange')
axes[1, 0].set_title('Recall (%)')
axes[1, 0].set_xlim(80, 105)

# F1-Score
axes[1, 1].barh(perf_df['Modèle'], perf_df['F1-Score'], color='lightcoral')
axes[1, 1].set_title('F1-Score (%)')
axes[1, 1].set_xlim(80, 105)

plt.tight_layout()
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("""
**Avertissement:** Cette application est à des fins éducatives et ne doit pas remplacer un avis médical professionnel.
Consultez toujours un professionnel de santé pour un diagnostic précis.
""")
