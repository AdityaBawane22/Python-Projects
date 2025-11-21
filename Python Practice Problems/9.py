import pandas as pd
import numpy as np

data_pivot = {
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108],
    'LoyaltyStatus': ['Gold', 'Silver', 'Gold', 'Bronze', 'Silver', 'Gold', 'Bronze', 'Silver'],
    'Region': ['East', 'West', 'East', 'North', 'East', 'West', 'North', 'West'],
    'TransactionAmount': [150.00, 50.00, 250.00, 20.00, 75.00, 100.00, 45.00, 125.00]
}
df_analysis = pd.DataFrame(data_pivot)

def pivot_tables(df):

    #rep_w_z = df.replace([''])
    piv_tab = df.pivot_table(
        values = 'TransactionAmount',
        index = 'LoyaltyStatus',
        columns = 'Region',
        aggfunc = 'mean'
    )

    piv_tab = piv_tab.fillna(0)
    return piv_tab
result = pivot_tables(df_analysis)
print(result)