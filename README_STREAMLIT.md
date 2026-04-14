# Interface Streamlit - Prédiction des Maladies Cardiaques

## Description
Application web interactive pour tester les modèles de Machine Learning de prédiction des maladies cardiaques avec un formulaire de saisie complet.

## Fonctionnalités

###  Formulaire de Saisie Complet
- **Données démographiques**: Âge, genre
- **Données cliniques**: Cholestérol, pression artérielle, fréquence cardiaque
- **Style de vie**: Tabagisme, alcool, exercice physique
- **Antécédents**: Familiaux, diabète, obésité
- **Symptômes**: Niveau de stress, taux de sucre, angine, douleur thoracique

###  Modèles Disponibles
- Random Forest (100% accuracy)
- AdaBoost (100% accuracy) 
- Gradient Boosting (100% accuracy)
- SVM (96% accuracy)
- Decision Tree (100% accuracy)
- KNN (93.5% accuracy)
- GaussianNB (92% accuracy)
- Régression Logistique (88.5% accuracy)
- ExtraTrees (96.5% accuracy)

###  Visualisations
- Graphique circulaire des probabilités
- Tableau comparatif des performances
- Graphiques des métriques (Accuracy, Precision, Recall, F1-Score)

## Installation

1. Installer les dépendances:
```bash
pip install -r requirements.txt
```

2. Lancer l'application:
```bash
streamlit run streamlit_app.py
```

## Utilisation

1. **Sélection du modèle**: Choisissez un modèle dans la sidebar
2. **Saisie des données**: Remplissez le formulaire avec les données du patient
3. **Prédiction**: Cliquez sur "Lancer la Prédiction"
4. **Résultats**: Visualisez les résultats et les probabilités

## Structure des Données

L'application utilise les 15 variables cliniques suivantes:
- `age`: Âge du patient
- `gender`: Genre (0=Femme, 1=Homme)
- `chol`: Cholestérol (mg/dL)
- `bp`: Pression artérielle (mmHg)
- `hr`: Fréquence cardiaque (bpm)
- `smoke`: Tabagisme (0=Jamais, 1=Ancien, 2=Actuel)
- `alcohol`: Alcool (0=Aucune, 1=Légère, 2=Modérée, 3=Élevée)
- `exercise`: Heures d'exercice/semaine
- `family_hist`: Antécédents familiaux (0=Non, 1=Oui)
- `diabetes`: Diabète (0=Non, 1=Oui)
- `obesity`: Obésité (0=Non, 1=Oui)
- `stress`: Niveau de stress (1-10)
- `sugar`: Taux de sucre (mg/dL)
- `angina`: Angine induite (0=Non, 1=Oui)
- `cp`: Type de douleur thoracique (0-4)

## Performances des Modèles

| Modèle | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| Random Forest | 100% | 100% | 100% | 100% |
| AdaBoost | 100% | 100% | 100% | 100% |
| Gradient Boosting | 100% | 100% | 100% | 100% |
| SVM | 96% | 92.3% | 92.3% | 92.3% |
| Decision Tree | 100% | 100% | 100% | 100% |
| KNN | 93.5% | 93.3% | 89.7% | 91.5% |
| GaussianNB | 92% | 95.6% | 83.3% | 89.0% |
| Régression Logistique | 88.5% | 86.7% | 83.3% | 85.0% |
| ExtraTrees | 96.5% | 100% | 91.0% | 95.3% |

## Avertissement

Cette application est à des fins éducatives et ne doit pas remplacer un avis médical professionnel. Consultez toujours un professionnel de santé pour un diagnostic précis.
