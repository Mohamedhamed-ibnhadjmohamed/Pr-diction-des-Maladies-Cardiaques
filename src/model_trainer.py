"""
Model Trainer Module
Module pour entraîner et évaluer les modèles de machine learning
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, Tuple, Optional
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score
import joblib


class ModelTrainer:
    """Classe pour entraîner et évaluer les modèles de ML"""
    
    def __init__(self, random_state: int = 42):
        """
        Initialise le ModelTrainer
        
        Args:
            random_state (int): Seed pour la reproductibilité
        """
        self.random_state = random_state
        self.models = {}
        self.scaler = None
        self.best_model = None
        self.best_model_name = None
        self.results = {}
    
    def initialize_models(self) -> Dict[str, Any]:
        """
        Initialise les différents modèles de ML
        
        Returns:
            Dict[str, Any]: Dictionnaire des modèles initialisés
        """
        self.models = {
            'Logistic Regression': LogisticRegression(random_state=self.random_state),
            'Random Forest': RandomForestClassifier(random_state=self.random_state),
            'Gradient Boosting': GradientBoostingClassifier(random_state=self.random_state),
            'SVM': SVC(random_state=self.random_state, probability=True),
            'KNN': KNeighborsClassifier()
        }
        
        return self.models
    
    def prepare_data(self, X: pd.DataFrame, y: pd.Series, test_size: float = 0.2) -> Tuple:
        """
        Prépare les données pour l'entraînement
        
        Args:
            X (pd.DataFrame): Features
            y (pd.Series): Target
            test_size (float): Proportion pour le test set
            
        Returns:
            Tuple: X_train, X_test, y_train, y_test
        """
        # Division en train/test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state, stratify=y
        )
        
        # Standardisation
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        return X_train_scaled, X_test_scaled, y_train, y_test
    
    def train_models(self, X_train: np.ndarray, y_train: pd.Series) -> Dict[str, Dict]:
        """
        Entraîne tous les modèles et retourne les résultats
        
        Args:
            X_train (np.ndarray): Features d'entraînement
            y_train (pd.Series): Target d'entraînement
            
        Returns:
            Dict[str, Dict]: Résultats pour chaque modèle
        """
        if not self.models:
            self.initialize_models()
        
        self.results = {}
        
        for name, model in self.models.items():
            print(f"Entraînement du modèle: {name}")
            
            # Entraînement
            model.fit(X_train, y_train)
            
            # Validation croisée
            cv_scores = cross_val_score(model, X_train, y_train, cv=5)
            
            self.results[name] = {
                'model': model,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std()
            }
            
            print(f"CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
        
        return self.results
    
    def evaluate_models(self, X_test: np.ndarray, y_test: pd.Series) -> Dict[str, Dict]:
        """
        Évalue les modèles sur l'ensemble de test
        
        Args:
            X_test (np.ndarray): Features de test
            y_test (pd.Series): Target de test
            
        Returns:
            Dict[str, Dict]: Résultats d'évaluation
        """
        evaluation_results = {}
        
        for name, result in self.results.items():
            model = result['model']
            y_pred = model.predict(X_test)
            
            # Calcul des métriques
            accuracy = accuracy_score(y_test, y_pred)
            
            # Pour l'AUC, on a besoin des probabilités
            if hasattr(model, 'predict_proba'):
                y_pred_proba = model.predict_proba(X_test)[:, 1]
            else:
                y_pred_proba = model.decision_function(X_test)
            
            auc_score = roc_auc_score(y_test, y_pred_proba)
            
            evaluation_results[name] = {
                'accuracy': accuracy,
                'auc': auc_score,
                'predictions': y_pred,
                'probabilities': y_pred_proba
            }
            
            print(f"{name} - Accuracy: {accuracy:.4f}, AUC: {auc_score:.4f}")
        
        # Mise à jour des résultats
        for name in evaluation_results:
            self.results[name].update(evaluation_results[name])
        
        return evaluation_results
    
    def select_best_model(self, metric: str = 'accuracy') -> Tuple[str, Any]:
        """
        Sélectionne le meilleur modèle selon la métrique spécifiée
        
        Args:
            metric (str): Métrique pour la sélection ('accuracy' ou 'auc')
            
        Returns:
            Tuple[str, Any]: Nom du meilleur modèle et le modèle lui-même
        """
        if not self.results:
            raise ValueError("Aucun résultat disponible. Entraînez les modèles d'abord.")
        
        best_score = -1
        best_name = None
        
        for name, result in self.results.items():
            score = result.get(metric, 0)
            if score > best_score:
                best_score = score
                best_name = name
        
        self.best_model_name = best_name
        self.best_model = self.results[best_name]['model']
        
        print(f"Meilleur modèle: {best_name} ({metric}: {best_score:.4f})")
        return best_name, self.best_model
    
    def get_feature_importance(self, feature_names: list) -> Optional[pd.DataFrame]:
        """
        Retourne l'importance des features si disponible
        
        Args:
            feature_names (list): Noms des features
            
        Returns:
            Optional[pd.DataFrame]: Importance des features ou None
        """
        if not self.best_model or not hasattr(self.best_model, 'feature_importances_'):
            return None
        
        importance = pd.DataFrame({
            'Feature': feature_names,
            'Importance': self.best_model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        return importance
    
    def save_model(self, model_path: str = "../models/best_model.pkl", 
                   scaler_path: str = "../models/scaler.pkl") -> None:
        """
        Sauvegarde le meilleur modèle et le scaler
        
        Args:
            model_path (str): Chemin pour sauvegarder le modèle
            scaler_path (str): Chemin pour sauvegarder le scaler
        """
        if self.best_model is None:
            raise ValueError("Aucun modèle à sauvegarder")
        
        import os
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        joblib.dump(self.best_model, model_path)
        if self.scaler:
            joblib.dump(self.scaler, scaler_path)
        
        print(f"Modèle sauvegardé: {model_path}")
        print(f"Scaler sauvegardé: {scaler_path}")
    
    def load_model(self, model_path: str = "../models/best_model.pkl",
                   scaler_path: str = "../models/scaler.pkl") -> None:
        """
        Charge un modèle et un scaler sauvegardés
        
        Args:
            model_path (str): Chemin du modèle
            scaler_path (str): Chemin du scaler
        """
        self.best_model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        
        print(f"Modèle chargé: {model_path}")
        print(f"Scaler chargé: {scaler_path}")


if __name__ == "__main__":
    # Exemple d'utilisation
    from data_loader import DataLoader
    
    # Chargement des données
    loader = DataLoader()
    data = loader.load_data()
    X, y = loader.get_features_target()
    
    # Entraînement des modèles
    trainer = ModelTrainer()
    X_train, X_test, y_train, y_test = trainer.prepare_data(X, y)
    
    trainer.train_models(X_train, y_train)
    trainer.evaluate_models(X_test, y_test)
    
    # Sélection du meilleur modèle
    best_name, best_model = trainer.select_best_model()
    
    # Importance des features
    importance = trainer.get_feature_importance(X.columns)
    if importance is not None:
        print("\nTop 10 des features les plus importantes:")
        print(importance.head(10))
