# 📁 Structure du Projet ML Professionnel

## 🏗️ Architecture des dossiers

```
📂 Pr-diction-des-Maladies-Cardiaques/
├── 📊 data/                           # Données brutes et traitées
│   ├── heart_data.csv               # Dataset principal
│   ├── raw/                        # Données brutes originales
│   ├── processed/                   # Données prétraitées
│   └── external/                    # Données externes (validation)
│
├── 📓 notebooks/                       # Notebooks de développement
│   ├── 00_Pipeline_Complete.ipynb  # Pipeline ML complet (principal)
│   ├── 01_Analyse.ipynb          # Exploration simplifiée
│   ├── 02_Modele.ipynb           # Modélisation simplifiée
│   └── experiments/                 # Tests et expérimentations
│
├── 📂 src/                            # Code Python modulaire
│   ├── __init__.py
│   ├── data/                        # Modules de gestion des données
│   │   ├── loader.py              # Chargement et validation
│   │   ├── preprocessor.py        # Pipeline de preprocessing
│   │   └── validator.py           # Validation de données
│   ├── models/                      # Modules de modélisation
│   │   ├── baseline.py            # Modèles de base
│   │   ├── optimizer.py           # Optimisation hyperparamètres
│   │   └── evaluator.py           # Évaluation des modèles
│   ├── utils/                       # Utilitaires généraux
│   │   ├── metrics.py             # Métriques personnalisées
│   │   ├── visualization.py      # Fonctions de visualisation
│   │   └── helpers.py             # Fonctions utilitaires
│   └── pipeline/                     # Pipeline ML complet
│       ├── ml_pipeline.py         # Pipeline principal
│       └── config.py              # Configuration du pipeline
│
├── 📂 models/                          # Modèles entraînés et composants
│   ├── best_heart_model_final.pkl  # Meilleur modèle optimisé
│   ├── scaler_final.pkl            # Paramètres de standardisation
│   ├── label_encoders.pkl         # Encodeurs catégoriels
│   ├── model_metadata.json        # Métadonnées complètes
│   └── experiments/              # Historique des expérimentations
│
├── 📂 reports/                         # Rapports et visualisations
│   ├── figures/                   # Graphiques et figures
│   ├── tables/                    # Tableaux de résultats
│   └── documentation/             # Rapports techniques
│
├── 📂 tests/                           # Tests unitaires et d'intégration
│   ├── test_data.py                # Tests des modules de données
│   ├── test_models.py              # Tests des modèles
│   └── test_pipeline.py            # Tests du pipeline complet
│
├── 📂 docs/                            # Documentation technique
│   ├── api_reference.md           # Référence API
│   ├── user_guide.md             # Guide utilisateur
│   └── development_guide.md       # Guide développeur
│
├── 📂 deployment/                       # Fichiers de déploiement
│   ├── docker/                    # Configuration Docker
│   ├── api/                       # Interface API
│   └── monitoring/                # Scripts de monitoring
│
├── 📄 requirements.txt                 # Dépendances Python
├── 📄 requirements_PROFESSIONNEL.txt   # Dépendances versionnées
├── 📄 environment.yml                  # Environnement Conda
├── 📄 setup.py                        # Installation du package
├── 📄 README.md                       # Documentation principale
├── 📄 README_SIMPLE.md               # Version simplifiée
├── 📄 README_PROFESSIONNEL.md       # Version professionnelle
├── 📄 STRUCTURE_PROJET.md            # Ce fichier
├── 📄 GUIDE_DEBUTANT.md              # Guide débutants
├── 📄 .gitignore                      # Fichiers ignorés par Git
└── 📄 LICENSE                         # Licence du projet
```

## 📋 Description des composants

### 📊 `/data/` - Gestion des données
- **Données brutes** : Fichiers originaux non modifiés
- **Données traitées** : Résultats du preprocessing
- **Validation externe** : Datasets pour tests finaux

### 📓 `/notebooks/` - Développement itératif
- **Pipeline complet** : `00_Pipeline_Complete.ipynb` - Workflow professionnel
- **Notebooks éducatifs** : Versions simplifiées pour apprentissage
- **Expérimentations** : Tests d'hypothèses et nouveaux modèles

### 📂 `/src/` - Code modulaire et réutilisable
- **Data modules** : Chargement, preprocessing, validation
- **Models modules** : Définition, optimisation, évaluation
- **Utils modules** : Métriques, visualisations, helpers
- **Pipeline modules** : Workflow ML complet et configuration

### 📂 `/models/` - Artefacts ML
- **Modèles sauvegardés** : Format pickle pour réutilisation
- **Métadonnées** : Traçabilité complète des expérimentations
- **Historique** : Versioning des modèles et performances

### 📂 `/reports/` - Résultats et communication
- **Visualisations** : Graphiques pour rapports
- **Tableaux** : Résultats structurés
- **Documentation** : Rapports techniques et métier

### 📂 `/tests/` - Assurance qualité
- **Tests unitaires** : Validation des fonctions individuelles
- **Tests d'intégration** : Validation du pipeline complet
- **Tests de régression** : Non-régression des performances

### 📂 `/deployment/` - Production
- **Containerisation** : Docker pour déploiement
- **API** : Interface REST pour prédictions
- **Monitoring** : Scripts de surveillance

## 🔄 Workflow de développement

### 1. Phase d'exploration 📊
```bash
# Lancer notebook d'exploration
jupyter notebook notebooks/01_Analyse.ipynb

# Ou version complète
jupyter notebook notebooks/00_Pipeline_Complete.ipynb
```

### 2. Phase de développement 🛠️
```bash
# Développer dans src/
python -m src.pipeline.ml_pipeline

# Tests continus
pytest tests/ -v
```

### 3. Phase d'expérimentation 🔬
```bash
# Nouveaux modèles dans notebooks/experiments/
jupyter notebook notebooks/experiments/new_model.ipynb
```

### 4. Phase de production 🚀
```bash
# Déploiement
docker build -t heart-disease-prediction deployment/
docker run -p 8000:8000 heart-disease-prediction
```

## 📦 Configuration de l'environnement

### Développement local
```bash
# Environnement virtuel
python -m venv ml_env
source ml_env/bin/activate  # Linux/Mac
ml_env\Scripts\activate     # Windows

# Installation dépendances
pip install -r requirements_PROFESSIONNEL.txt
```

### Environnement Conda (recommandé)
```bash
# Création environnement
conda env create -f environment.yml
conda activate heart-disease-ml

# Installation dépendances additionnelles
pip install -r requirements_PROFESSIONNEL.txt
```

### Docker (production)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements_PROFESSIONNEL.txt .
RUN pip install -r requirements_PROFESSIONNEL.txt

COPY src/ ./src/
COPY models/ ./models/
COPY deployment/api/ ./api/

EXPOSE 8000
CMD ["python", "-m", "api.main"]
```

## 📋 Bonnes pratiques de développement

### 1. Versioning et traçabilité
- **Git flow** : main → develop → feature → release
- **Tags** : v1.0.0, v1.1.0, etc.
- **Commits** : Messages clairs et structurés

### 2. Code quality
- **Linting** : flake8, black pour formatage
- **Typage** : Annotations de type avec mypy
- **Documentation** : Docstrings pour toutes fonctions

### 3. Tests automatisés
- **Couverture** : >90% visée
- **CI/CD** : GitHub Actions ou GitLab CI
- **Tests de performance** : Benchmarking des modèles

### 4. Reproductibilité
- **Random seeds** : Fixées pour reproductibilité
- **Configuration** : Fichiers de config séparés
- **Environnement** : Spécifications précises des dépendances

## 📊 Métriques et monitoring

### KPIs de développement
- **Couverture de tests** : Pourcentage de code testé
- **Performance des modèles** : Accuracy, AUC, temps d'inférence
- **Complexité du code** : Maintenabilité et évolutivité

### Monitoring en production
- **Latence** : Temps de réponse des prédictions
- **Taux d'erreur** : Erreurs par minute/heure
- **Drift detection** : Changements dans distribution des données

## 🚀 Pipeline CI/CD

### GitHub Actions example
```yaml
name: ML Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements_PROFESSIONNEL.txt
    - name: Run tests
      run: |
        pytest tests/ -v --cov=src
    - name: Upload coverage
      uses: codecov/codecov-action@v1

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to production
      run: |
        # Script de déploiement
        echo "Deployment successful"
```

## 📚 Documentation technique

### API Reference
```python
# Exemple d'utilisation du pipeline
from src.pipeline.ml_pipeline import MLPipeline

# Initialisation
pipeline = MLPipeline(config_path='config/pipeline_config.json')

# Exécution complète
results = pipeline.run(data_path='data/heart_data.csv')

# Prédiction sur nouvelles données
predictions = pipeline.predict(new_data)
```

### Guide de contribution
1. Forker le projet
2. Créer une branche feature
3. Développer avec tests
4. Soumettre une pull request
5. Validation par code review

---

Cette structure professionnelle assure :
- **Scalabilité** : Architecture modulaire et extensible
- **Maintenabilité** : Code organisé et documenté
- **Reproductibilité** : Configuration et versioning rigoureux
- **Déploiement** : Pipeline CI/CD automatisé
- **Qualité** : Tests et monitoring continus
