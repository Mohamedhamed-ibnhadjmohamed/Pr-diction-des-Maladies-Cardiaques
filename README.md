# Prédiction des Maladies Cardiaques

## Auteur
Mohamed Hamed Ibn Hadj Mohamed

## Description du Projet
Ce projet de machine learning vise à prédire la présence de maladies cardiaques chez les patients en utilisant des algorithmes de classification. Le projet utilise des techniques d'analyse exploratoire des données, de préprocessing et de modélisation pour développer un modèle prédictif performant.

## Dataset
Le dataset utilisé provient du fichier ML.pdf et contient des données médicales relatives aux facteurs de risque de maladies cardiaques.

## Problématique
L'objectif est de développer un modèle de machine learning capable de prédire avec précision si un patient est à risque de développer une maladie cardiaque, en se basant sur ses caractéristiques médicales et démographiques.

## Structure du Repository

```
├── data/                 # Dataset ou script de téléchargement
├── notebooks/            # Notebooks Jupyter commentés
│   ├── 01_EDA.ipynb      # Analyse Exploratoire des Données
│   └── 02_Modeling.ipynb # Préprocessing et Modélisation
├── src/                  # Scripts Python modulaires (Bonus)
├── requirements.txt      # Dépendances Python
├── environment.yml       # Environnement Conda (Optionnel)
├── README.md             # Documentation du projet
├── Presentation.pdf      # Slides de soutenance
└── .gitignore            # Fichiers ignorés par Git
```

## Installation

### Méthode 1: Avec pip
```bash
pip install -r requirements.txt
```

### Méthode 2: Avec Conda (optionnel)
```bash
conda env create -f environment.yml
conda activate votre-environnement
```

### Lancement des Notebooks
```bash
jupyter notebook
```
Naviguez vers le dossier `notebooks/` et exécutez les notebooks dans l'ordre:
1. `01_EDA.ipynb` - Analyse exploratoire des données
2. `02_Modeling.ipynb` - Préprocessing et modélisation

## Résultats Obtenus
*À compléter après exécution des notebooks*

## Technologies Utilisées
- Python
- Jupyter Notebook
- Scikit-learn
- Pandas
- NumPy
- Matplotlib/Seaborn

## Livrables Attendus

### 1. Les Notebooks (/notebooks)
- Code en Python
- Structure claire avec des titres (Markdown)
- Commentaires explicatifs pour chaque étape logique
- Cellules exécutées avec résultats visibles

### 2. Le fichier README.md
- Titre du projet
- Auteur
- Description du dataset et source
- Problématique abordée
- Guide d'installation
- Résumé des résultats obtenus

### 3. L'Environnement Technique
- Fichier requirements.txt fonctionnel
- Commande: `pip install -r requirements.txt`