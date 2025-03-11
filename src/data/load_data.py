import pandas as pd

def load_raw_data(filepath="data/raw/fruit_data_with_colors.txt"):
    print(f"Loading file from: {filepath}")
    
    # Try using '\t' as the delimiter since columns are tab-separated
    df = pd.read_csv(filepath, delimiter="\t")  

    print("Loaded DataFrame columns:", df.columns)  # Debugging output
    return df
