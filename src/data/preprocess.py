import joblib
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, scaler_filepath="models/scaler.joblib"):
    print("Available columns:", df.columns)  # Debugging step

    numerical_features = ['mass', 'width', 'height', 'color_score']
    
    # Check if numerical_features exist in df
    missing_cols = [col for col in numerical_features if col not in df.columns]
    if missing_cols:
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # Ensure the directory exists before saving the scaler
    import os
    os.makedirs(os.path.dirname(scaler_filepath), exist_ok=True)

    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    # Save the scaler
    joblib.dump(scaler, scaler_filepath)
    print(f"Scaler saved to {scaler_filepath}")

    return df
