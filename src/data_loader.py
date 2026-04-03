"""
Data Loader Module
Module pour charger et préparer les données
"""

import pandas as pd
import numpy as np
from typing import Optional, Tuple


class DataLoader:
    """Classe pour charger et préparer les données de maladies cardiaques"""
    
    def __init__(self, data_path: str = "../data/heart_disease_dataset.csv"):
        """
        Initialise le DataLoader
        
        Args:
            data_path (str): Chemin vers le fichier de données
        """
        self.data_path = data_path
        self.data = None
    
    def load_data(self) -> pd.DataFrame:
        """
        Charge les données depuis le fichier CSV
        
        Returns:
            pd.DataFrame: DataFrame contenant les données
        """
        try:
            self.data = pd.read_csv(self.data_path)
            print(f"Données chargées avec succès: {self.data.shape}")
            return self.data
        except FileNotFoundError:
            print(f"Fichier non trouvé: {self.data_path}")
            # Création de données d'exemple pour démonstration
            self.data = self._create_sample_data()
            return self.data
    
    def _create_sample_data(self) -> pd.DataFrame:
        """
        Crée un dataset d'exemple pour démonstration
        
        Returns:
            pd.DataFrame: DataFrame d'exemple
        """
        np.random.seed(42)
        n_samples = 1000
        
        data = {
            'age': np.random.randint(25, 80, n_samples),
            'sex': np.random.choice([0, 1], n_samples),
            'cp': np.random.choice([0, 1, 2, 3], n_samples),
            'trestbps': np.random.randint(90, 200, n_samples),
            'chol': np.random.randint(150, 400, n_samples),
            'fbs': np.random.choice([0, 1], n_samples),
            'restecg': np.random.choice([0, 1, 2], n_samples),
            'thalach': np.random.randint(70, 200, n_samples),
            'exang': np.random.choice([0, 1], n_samples),
            'oldpeak': np.random.uniform(0, 6, n_samples),
            'slope': np.random.choice([0, 1, 2], n_samples),
            'ca': np.random.choice([0, 1, 2, 3], n_samples),
            'thal': np.random.choice([0, 1, 2, 3], n_samples),
            'target': np.random.choice([0, 1], n_samples)
        }
        
        self.data = pd.DataFrame(data)
        print("Dataset d'exemple créé pour démonstration")
        return self.data
    
    def get_features_target(self, target_column: str = "Heart Disease") -> Tuple[pd.DataFrame, pd.Series]:
        """
        Sépare les features et la variable cible
        
        Args:
            target_column (str): Nom de la colonne cible
            
        Returns:
            Tuple[pd.DataFrame, pd.Series]: Features et target
        """
        if self.data is None:
            self.load_data()
        
        X = self.data.drop(target_column, axis=1)
        y = self.data[target_column]
        
        return X, y
    
    def get_data_info(self) -> dict:
        """
        Retourne des informations sur les données
        
        Returns:
            dict: Informations sur le dataset
        """
        if self.data is None:
            self.load_data()
        
        info = {
            "shape": self.data.shape,
            "columns": list(self.data.columns),
            "dtypes": self.data.dtypes.to_dict(),
            "missing_values": self.data.isnull().sum().to_dict(),
            "numeric_columns": list(self.data.select_dtypes(include=[np.number]).columns),
            "categorical_columns": list(self.data.select_dtypes(include=['object']).columns)
        }
        
        return info


if __name__ == "__main__":
    # Exemple d'utilisation
    loader = DataLoader()
    data = loader.load_data()
    print("Aperçu des données:")
    print(data.head())
    
    info = loader.get_data_info()
    print(f"\nInformations: {info}")
