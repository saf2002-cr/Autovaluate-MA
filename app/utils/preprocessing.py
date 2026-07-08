import numpy as np
import pandas as pd

# Colonnes exactes issues de votre fichier X_train.csv
MODEL_EXPECTED_COLUMNS = [
    'Annee', 'Kilometrage', 'Usage_Intensity',
    'Marque_Alfa', 'Marque_Audi', 'Marque_Autre', 'Marque_BMW', 'Marque_Citroën',
    'Marque_Dacia', 'Marque_Fiat', 'Marque_Ford', 'Marque_Hyundai', 'Marque_Jaguar',
    'Marque_Jeep', 'Marque_Kia', 'Marque_Land Rover', 'Marque_Mercedes-Benz',
    'Marque_Nissan', 'Marque_Opel', 'Marque_Peugeot', 'Marque_Renault',
    'Marque_Seat', 'Marque_Skoda', 'Marque_Toyota', 'Marque_Volkswagen', 'Marque_Volvo',
    'Ville_Agadir', 'Ville_Autres', 'Ville_Casablanca', 'Ville_Marrakech', 'Ville_Rabat', 'Ville_Tanger',
    'Transmission_Automatique', 'Transmission_Manuelle',
    'Carburant_Diesel', 'Carburant_Electrifié', 'Carburant_Essence'
]

def map_and_encode_inputs(raw_inputs: dict) -> pd.DataFrame:
    """
    Prend les entrées brutes de l'application Streamlit, applique le feature engineering
    et génère le vecteur exact avec le One-Hot Encoding aligné sur le X_train.
    """
    # Étape 1: Initialiser un DataFrame vide avec toutes les colonnes du modèle à False/0
    encoded_df = pd.DataFrame(False, index=[0], columns=MODEL_EXPECTED_COLUMNS)
    
    # Étape 2: Assigner et calculer les variables numériques brutes
    annee = int(raw_inputs['Annee'])
    kilometrage = float(raw_inputs['Kilometrage'])
    
    encoded_df['Annee'] = annee
    encoded_df['Kilometrage'] = kilometrage
    
    # Étape 3: Feature Engineering de 'Usage_Intensity' tel que fait dans votre notebook
    # Attention : s'assurer d'éviter la division par zéro si l'âge calculé est égal à 0
    age = 2026 - annee
    if age <= 0:
        age = 1
    encoded_df['Usage_Intensity'] = kilometrage / age
    
    # Étape 4: Assigner True (1) pour les variables catégorielles correspondantes (One-Hot Encoding)
    marque_col = f"Marque_{raw_inputs['Marque']}"
    ville_col = f"Ville_{raw_inputs['Ville']}"
    trans_col = f"Transmission_{raw_inputs['Transmission']}"
    carb_col = f"Carburant_{raw_inputs['Carburant']}"
    
    # Vérification dynamique pour éviter les crashs si une option est absente
    if marque_col in encoded_df.columns:
        encoded_df[marque_col] = True
    else:
        # Repli sur 'Marque_Autre' si la marque saisie n'est pas explicitement dans les colonnes principales
        if 'Marque_Autre' in encoded_df.columns:
            encoded_df['Marque_Autre'] = True
            
    if ville_col in encoded_df.columns:
        encoded_df[ville_col] = True
    else:
        # Repli sur 'Ville_Autres' si la ville n'est pas dans le top 6
        if 'Ville_Autres' in encoded_df.columns:
            encoded_df['Ville_Autres'] = True
            
    if trans_col in encoded_df.columns:
        encoded_df[trans_col] = True
        
    if carb_col in encoded_df.columns:
        encoded_df[carb_col] = True
        
    return encoded_df