# Data Folder

Ce dossier contient les données utilisées pour le projet de prédiction des maladies cardiaques.

## Structure

```
data/
├── README.md           # Ce fichier
├── heart_disease.csv   # Dataset principal (à ajouter)
└── raw/               # Données brutes (optionnel)
```

## Instructions

1. **Ajoutez votre dataset principal** dans ce dossier sous le nom `heart_disease.csv`
2. Le format attendu est un fichier CSV avec les colonnes suivantes:
   - `age`: Âge du patient
   - `sex`: Sexe (0=femme, 1=homme)
   - `cp`: Type de douleur thoracique (0-3)
   - `trestbps`: Pression artérielle au repos (mm Hg)
   - `chol`: Cholestérol sérique (mg/dl)
   - `fbs`: Glycémie à jeun > 120 mg/dl (0=non, 1=oui)
   - `restecg`: Résultats électrocardiographiques au repos (0-2)
   - `thalach`: Fréquence cardiaque maximale atteinte
   - `exang`: Angine induite par l'exercice (0=non, 1=oui)
   - `oldpeak`: Dépression ST induite par l'exercice
   - `slope`: Pente du segment ST à l'effort (0-2)
   - `ca`: Nombre de vaisseaux colorés par fluoroscopie (0-3)
   - `thal`: Thalassémie (0-3)
   - `target`: Variable cible (0=pas de maladie, 1=maladie)

## Sources de données possibles

- [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease)
- [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)

## Notes

- Assurez-vous que les données sont nettoyées et prêtes à l'emploi
- Les valeurs manquantes doivent être traitées avant l'utilisation
- Le dataset doit contenir suffisamment d'exemples pour chaque classe
