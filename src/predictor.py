"""
Assistant de Prédiction Cardiaque
Module conçu pour aider les professionnels de santé à évaluer le risque de maladies cardiaques
avec une approche humaine et compréhensible pour les patients.
"""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Any
import joblib


class HeartDiseasePredictor:
    """Votre assistant intelligent pour l'évaluation du risque cardiaque"""
    
    def __init__(self, model_path: str = "../models/best_model.pkl",
                 scaler_path: str = "../models/scaler.pkl"):
        """
        Initialise votre assistant de prédiction cardiaque
        
        Args:
            model_path (str): Chemin vers votre modèle entraîné
            scaler_path (str): Chemin vers votre outil de normalisation
        """
        self.model = None
        self.scaler = None
        self.feature_names = None
        self.load_models(model_path, scaler_path)
    
    def load_models(self, model_path: str, scaler_path: str) -> None:
        """
        Charge votre système d'analyse cardiaque
        
        Args:
            model_path (str): Emplacement de votre modèle
            scaler_path (str): Emplacement de votre normalisateur
        """
        try:
            self.model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            print("Votre assistant cardiaque est prêt à vous aider !")
        except FileNotFoundError as e:
            print(f"Je n'ai pas pu charger les fichiers nécessaires : {e}")
            raise
    
    def set_feature_names(self, feature_names: List[str]) -> None:
        """
        Configure les informations que je vais analyser
        
        Args:
            feature_names (List[str]): Liste des caractéristiques à examiner
        """
        self.feature_names = feature_names
        print(f"Je vais maintenant analyser {len(feature_names)} facteurs de santé")
    
    def predict_single(self, patient_data: Dict[str, Union[int, float]]) -> Dict[str, Any]:
        """
        Analyse la santé cardiaque d'un patient
        
        Args:
            patient_data (Dict[str, Union[int, float]]): Informations sur le patient
            
        Returns:
            Dict[str, Any]: Mon analyse détaillée pour le patient
        """
        if self.model is None:
            raise ValueError("Je ne suis pas encore initialisé, veuillez charger les modèles d'abord")
        
        # Préparation des données pour l'analyse
        df = pd.DataFrame([patient_data])
        
        # Vérification que j'ai toutes les informations nécessaires
        if self.feature_names:
            missing_features = set(self.feature_names) - set(df.columns)
            if missing_features:
                raise ValueError(f"⚠️ Il me manque des informations importantes : {missing_features}")
            
            # Organisation des données dans le bon ordre
            df = df[self.feature_names]
        
        # Normalisation pour une analyse précise
        if self.scaler:
            df_scaled = self.scaler.transform(df)
        else:
            df_scaled = df
        
        # Mon analyse prédictive
        prediction = self.model.predict(df_scaled)[0]
        
        # Calcul de ma confiance dans cette prédiction
        if hasattr(self.model, 'predict_proba'):
            probability = self.model.predict_proba(df_scaled)[0]
        else:
            probability = None
        
        # Résultat exprimé de manière compréhensible
        if prediction == 1:
            message = "J'ai détecté un risque de maladie cardiaque"
            conseil = "Je vous recommande de consulter un cardiologue"
        else:
            message = "Votre cœur semble en bonne santé"
            conseil = "Continuez à prendre soin de votre santé cardiaque"
        
        result = {
            'prediction': int(prediction),
            'message': message,
            'conseil': conseil,
            'confidence': probability.tolist() if probability is not None else None
        }
        
        return result
    
    def predict_batch(self, patient_data_list: List[Dict[str, Union[int, float]]]) -> List[Dict[str, Any]]:
        """
        Analyse la santé cardiaque de plusieurs patients
        
        Args:
            patient_data_list (List[Dict[str, Union[int, float]]]): Liste des informations patients
            
        Returns:
            List[Dict[str, Any]]: Mes analyses pour chaque patient
        """
        print(f"Je vais analyser la santé cardiaque de {len(patient_data_list)} patient(s)...")
        results = []
        
        for i, patient_data in enumerate(patient_data_list, 1):
            print(f"  Analyse du patient {i}/{len(patient_data_list)}...")
            result = self.predict_single(patient_data)
            results.append(result)
        
        print("J'ai terminé toutes mes analyses cardiaques !")
        return results
    
    def predict_from_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Analyse un groupe de patients à partir de leurs données
        
        Args:
            df (pd.DataFrame): Tableau avec les informations des patients
            
        Returns:
            pd.DataFrame: Tableau enrichi avec mes analyses cardiaques
        """
        if self.model is None:
            raise ValueError("Je ne suis pas encore prêt à analyser, veuillez m'initialiser d'abord")
        
        print(f"Je commence l'analyse de {len(df)} patient(s)...")
        
        # Copie pour préserver les données originales
        df_result = df.copy()
        
        # Vérification que j'ai toutes les informations nécessaires
        if self.feature_names:
            missing_features = set(self.feature_names) - set(df.columns)
            if missing_features:
                raise ValueError(f"⚠️ Il me manque des informations importantes : {missing_features}")
            
            # Organisation des données dans le bon ordre pour mon analyse
            df_ordered = df[self.feature_names]
        else:
            df_ordered = df
        
        # Préparation des données pour une analyse précise
        if self.scaler:
            df_scaled = self.scaler.transform(df_ordered)
        else:
            df_scaled = df_ordered
        
        # Mon analyse cardiaque pour tous les patients
        predictions = self.model.predict(df_scaled)
        df_result['prediction'] = predictions
        df_result['resultat'] = df_result['prediction'].apply(
            lambda x: 'Risque cardiaque détecté' if x == 1 else 'Cœur en bonne santé'
        )
        
        # Mes niveaux de confiance si disponibles
        if hasattr(self.model, 'predict_proba'):
            probabilities = self.model.predict_proba(df_scaled)
            df_result['confiance_sante'] = probabilities[:, 0]
            df_result['confiance_risque'] = probabilities[:, 1]
        
        print("Mon analyse cardiaque est terminée !")
        return df_result
    
    def get_risk_assessment(self, patient_data: Dict[str, Union[int, float]]) -> Dict[str, Any]:
        """
        Fournit une évaluation complète et personnalisée du risque cardiaque
        
        Args:
            patient_data (Dict[str, Union[int, float]]): Informations complètes du patient
            
        Returns:
            Dict[str, Any]: Mon évaluation détaillée et personnalisée
        """
        print("Je prépare votre évaluation cardiaque personnalisée...")
        
        # D'abord, je fais mon analyse de base
        prediction_result = self.predict_single(patient_data)
        
        # Ensuite, j'identifie les facteurs de risque spécifiques
        risk_factors = []
        
        # Analyse détaillée des facteurs de risque
        if patient_data.get('age', 0) > 65:
            risk_factors.append("Âge avancé (plus de 65 ans)")
        
        if patient_data.get('sex', 0) == 1:  # Homme
            risk_factors.append("Sexe masculin (risque statistiquement plus élevé)")
        
        if patient_data.get('chol', 0) > 240:  # Cholestérol élevé
            risk_factors.append("Cholestérol élevé (plus de 240 mg/dL)")
        
        if patient_data.get('trestbps', 0) > 140:  # Pression artérielle élevée
            risk_factors.append("Pression artérielle élevée (plus de 140 mmHg)")
        
        if patient_data.get('fbs', 0) == 1:  # Glycémie élevée
            risk_factors.append("Glycémie à jeun élevée")
        
        # Évaluation personnalisée du niveau de risque
        if prediction_result['prediction'] == 1:
            if prediction_result['confidence']:
                risk_level = prediction_result['confidence'][1]
                if risk_level > 0.8:
                    risk_category = "Élevé - Attention particulière requise"
                    explanation = "Votre risque est significatif, une consultation rapide est recommandée"
                elif risk_level > 0.6:
                    risk_category = "Modéré-Élevé - Surveillance nécessaire"
                    explanation = "Votre risque est modéré, une consultation médicale est conseillée"
                else:
                    risk_category = "Modéré - Prévention importante"
                    explanation = "Un risque modéré qui nécessite une attention particulière"
            else:
                risk_category = "Risque présent"
                explanation = "J'ai détecté un risque qui mérite votre attention"
        else:
            risk_category = "Faible - Continuez vos efforts"
            explanation = "Votre risque est faible, continuez à prendre soin de votre cœur"
        
        # Mes recommandations personnalisées
        recommendations = self._get_personalized_recommendations(risk_factors, risk_category)
        
        assessment = {
            'analyse_principale': prediction_result,
            'niveau_risque': risk_category,
            'explication': explanation,
            'facteurs_risque': risk_factors,
            'conseils_personnalises': recommendations,
            'message_encouragement': self._get_encouragement(risk_category)
        }
        
        print("Votre évaluation personnalisée est prête !")
        return assessment
    
    def _get_personalized_recommendations(self, risk_factors: List[str], risk_category: str) -> List[str]:
        """
        Crée des recommandations personnalisées et encourageantes
        
        Args:
            risk_factors (List[str]): Liste des facteurs de risque identifiés
            risk_category (str): Niveau de risque évalué
            
        Returns:
            List[str]: Mes conseils personnalisés pour vous
        """
        recommendations = []
        
        # Recommandations selon le niveau de risque
        if "Élevé" in risk_category:
            recommendations.append("Prenez rendez-vous avec un cardiologue dès que possible")
            recommendations.append("Faites un bilan cardiovasculaire complet rapidement")
            recommendations.append("N'attendez pas si vous ressentez des symptômes")
        elif "Modéré" in risk_category:
            recommendations.append("Consultez votre médecin traitant pour un bilan")
            recommendations.append("Envisagez un suivi régulier avec un spécialiste")
        
        # Conseils spécifiques selon les facteurs de risque
        if "Âge avancé" in str(risk_factors):
            recommendations.append("Prévoyez des check-ups médicaux réguliers")
            recommendations.append("Discutez de la prévention avec votre médecin")
        
        if "Cholestérol élevé" in str(risk_factors):
            recommendations.append("Adoptez une alimentation riche en fruits et légumes")
            recommendations.append("Pratiquez une activité physique régulière (30min/jour)")
            recommendations.append("Privilégiez les poissons gras et les oméga-3")
        
        if "Pression artérielle élevée" in str(risk_factors):
            recommendations.append("Réduisez votre consommation de sel")
            recommendations.append("Apprenez à gérer votre stress")
            recommendations.append("Maintenez un poids santé")
            recommendations.append("Surveillez régulièrement votre tension")
        
        if "Glycémie à jeun élevée" in str(risk_factors):
            recommendations.append("Limitez les sucres rapides et les produits transformés")
            recommendations.append("Privilégiez les aliments à index glycémique bas")
            recommendations.append("Faites des repas à heures régulières")
        
        # Si peu de facteurs de risque, conseils préventifs
        if len(risk_factors) <= 1:
            recommendations.append("Continuez vos bonnes habitudes de vie")
            recommendations.append("Maintenez une activité physique régulière")
            recommendations.append("Gardez une alimentation équilibrée")
            recommendations.append("Assurez-vous un bon sommeil (7-8h/nuit)")
        
        return recommendations
    
    def _get_encouragement(self, risk_category: str) -> str:
        """
        Donne un message d'encouragement personnalisé
        
        Args:
            risk_category (str): Niveau de risque
            
        Returns:
            str: Message d'encouragement personnalisé
        """
        if "Élevé" in risk_category:
            return "Vous avez déjà fait le premier pas en vous informant. Continuez à prendre soin de vous !"
        elif "Modéré" in risk_category:
            return "Votre santé est entre vos mains. Chaque petit pas compte énormément !"
        else:
            return "Continuez comme ça ! Votre cœur vous remercie chaque jour !"


if __name__ == "__main__":
    # Bienvenue dans votre assistant cardiaque personnel !
    print("Bonjour ! Je suis votre assistant intelligent pour l'évaluation de la santé cardiaque")
    print("Je suis là pour vous aider à mieux comprendre votre risque cardiaque")
    
    # Initialisation de votre assistant
    predictor = HeartDiseasePredictor()
    
    # Configuration des informations que je vais analyser
    feature_names = ['Age', 'Gender', 'Cholesterol', 'Blood Pressure', 'Heart Rate', 
                    'Smoking', 'Alcohol Intake', 'Exercise Hours', 'Family History', 
                    'Diabetes', 'Obesity', 'Stress Level', 'Blood Sugar', 
                    'Exercise Induced Angina', 'Chest Pain Type']
    predictor.set_feature_names(feature_names)
    
    # 📋 Exemple concret : analysons ensemble un patient
    print("\n" + "="*60)
    print("🔍 EXEMPLE : Analysons ensemble la santé cardiaque d'un patient")
    print("="*60)
    
    patient_data = {
        'Age': 55,
        'Gender': 'Male',
        'Cholesterol': 250,
        'Blood Pressure': 140,
        'Heart Rate': 75,
        'Smoking': 'Current',
        'Alcohol Intake': 'Moderate',
        'Exercise Hours': 3,
        'Family History': 'Yes',
        'Diabetes': 'No',
        'Obesity': 'No',
        'Stress Level': 5,
        'Blood Sugar': 90,
        'Exercise Induced Angina': 'No',
        'Chest Pain Type': 'Typical Angina'
    }
    
    print("\nInformations du patient analysé :")
    for key, value in patient_data.items():
        print(f"  • {key}: {value}")
    
    # Mon analyse rapide
    print("\n" + "-"*40)
    print("MON ANALYSE CARDIAQUE RAPIDE")
    print("-"*40)
    result = predictor.predict_single(patient_data)
    print(f"\nMon diagnostic : {result['message']}")
    print(f"Mon conseil : {result['conseil']}")
    if result['confidence']:
        print(f"Ma confiance : {result['confidence'][1]:.1%} dans cette évaluation")
    
    # Mon évaluation complète et personnalisée
    print("\n" + "-"*40)
    print("MON ÉVALUATION COMPLÈTE ET PERSONNALISÉE")
    print("-"*40)
    assessment = predictor.get_risk_assessment(patient_data)
    
    print(f"\nNiveau de risque : {assessment['niveau_risque']}")
    print(f"Mon explication : {assessment['explication']}")
    
    if assessment['facteurs_risque']:
        print(f"\nFacteurs de risque identifiés :")
        for factor in assessment['facteurs_risque']:
            print(f"  • {factor}")
    else:
        print("\nAucun facteur de risque majeur identifié")
    
    print(f"\nMes conseils personnalisés pour vous :")
    for i, conseil in enumerate(assessment['conseils_personnalises'], 1):
        print(f"  {i}. {conseil}")
    
    print(f"\nMon message d'encouragement :")
    print(f"  {assessment['message_encouragement']}")
    
    print("\n" + "="*60)
    print("Merci de m'avoir permis d'analyser votre santé cardiaque !")
    print("N'oubliez pas que je suis un outil d'aide et non un remplaçant médical")
    print("Consultez toujours un professionnel de santé pour un diagnostic complet")
    print("="*60)
