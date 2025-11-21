import pandas as pd
import numpy as np

data_clean = {
    'CustomerID': range(301, 311),
    'Age': [35, 42, 'N/A', 28, 55, 30, np.nan, 42, '-', 25],
    'Score': [85, 92, 70, 88, 95, 80, 75, 90, 65, 78]
}
df_survey = pd.DataFrame(data_clean)

def clean_and_impute_age(df):
    df = df.replace(['N/A', '-'], np.nan)
    df['Age'] = df['Age'].astype(float)
    mean_val = df['Age'].mean().round(1)
    df['Age'] = df['Age'].fillna(mean_val)
    
    df['Status'] = np.where((df['Age'] <= 35) & (df['Score'] >= 80), 'High', 'Low')
    return df
result = clean_and_impute_age(df_survey)
print(result)