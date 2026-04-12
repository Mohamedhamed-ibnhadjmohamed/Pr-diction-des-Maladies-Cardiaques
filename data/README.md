# Data Folder

Ce dossier contient les données utilisées pour le projet de prédiction des maladies cardiaques.

## Structure

```
data/
├── README.md           # Ce fichier
├── heart_disease.csv   # Data Folder
└── raw/               # Données brutes (optionnel)
```

## Datasets disponibles

### 1. `heart_disease_dataset.csv` - Données brutes
- **1000 patients** avec 16 caractéristiques cliniques
- **Variables démographiques** : Âge (25-79 ans), Genre
- **Facteurs de risque** : Cholestérol, Pression artérielle, Fréquence cardiaque
- **Style de vie** : Tabagisme, Alcool, Exercice, Stress
- **Antécédents** : Familiaux, Diabète, Obésité
- **Symptômes** : Angine d'effort, Type de douleur thoracique
- **Cible** : Présence (1) ou absence (0) de maladie cardiaque

### 2. `heart_disease_dataset1.csv` - Données prétraitées
- **Version nettoyée et encodée** pour utilisation ML directe
- **Variables numériques standardisées**
- **Prête pour l'entraînement** des modèles
- **340 valeurs manquantes** dans Alcohol Intake ont été imputées

## Colonnes disponibles

### Variables cliniques
- `age`: Âge du patient (25-79 ans)
- `gender`: Genre (Male/Female)
- `chol`: Cholestérol sérique (mg/dl)
- `bp`: Pression artérielle (mm Hg)
- `hr`: Fréquence cardiaque au repos (bpm)

### Style de vie
- `smoke`: Tabagisme (Never/Former/Current)
- `alcohol`: Consommation d'alcool (NaN/Moderate/Heavy)
- `exercise`: Exercice physique (Yes/No)
- `stress`: Niveau de stress (Low/Medium/High)

### Antécédents médicaux
- `family_hist`: Antécédents familiaux (Yes/No)
- `diabetes`: Diabète (Yes/No)
- `obesity`: Obésité (Yes/No)

### Symptômes
- `sugar`: Glycémie élevée (Yes/No)
- `angina`: Angine d'effort (Yes/No)
- `cp`: Type de douleur thoracique (0-3)

### Variable cible
- `target`: Présence (1) ou absence (0) de maladie cardiaque

## Traitement appliqué

### Prétraitement effectué
- **Encodage des variables catégorielles** : Gender, Smoking, Alcohol, etc.
- **Imputation des valeurs manquantes** : 340 valeurs dans Alcohol Intake
- **Standardisation** : MinMaxScaler et StandardScaler appliqués
- **Nettoyage des noms de colonnes** : Format standardisé

### Transformations spécifiques
- Gender : Male=1, Female=0
- Variables binaires : Yes=1, No=0
- Smoking : Never=0, Former=1, Current=2
- Alcohol : NaN=0, Moderate=1, Heavy=2

## Utilisation

Pour utiliser les données dans les notebooks :
```python
# Données prétraitées (recommandé)
df = pd.read_csv('../data/heart_disease_dataset1.csv')

# Données brutes (si besoin de refaire le preprocessing)
df_raw = pd.read_csv('../data/heart_disease_dataset.csv')
```

## Notes importantes

- **Dataset prétraité** prêt pour l'entraînement ML direct
- **Distribution équilibrée** des classes dans train/test split
- **Pas de data leakage** dans le preprocessing appliqué
- **Reproductibilité** garantie avec les transformations documentées
