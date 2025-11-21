"""Write a function, `analyze_monthly_revenue(df)`, that:

1.  **Converts** the `TransactionDate` column to the proper Pandas datetime object type using **`pd.to_datetime()`**.
2.  **Creates two new columns**: `'Year'` (as an integer) and `'Month'` (as an integer), extracting them from the `TransactionDate` column using the **`.dt` accessor** (e.g., `.dt.year`).
3.  **Groups** the DataFrame by both the `'Year'` and `'Month'` columns.
4.  **Aggregates** the data by calculating the **sum** of the `'Revenue'` for each Year-Month combination.
5.  Returns the resulting summary DataFrame, with `Year` and `Month` as the index.
"""

import pandas as pd

data_time = {
    'TransactionDate': ['2023-01-15', '2023-01-28', '2023-02-05', '2023-02-20', '2023-03-01', '2023-03-10', '2024-01-01', '2024-01-25'],
    'Revenue': [100, 50, 200, 150, 75, 125, 300, 400],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B']
}
df_time_series = pd.DataFrame(data_time)

def analyze_monthly_revenue(df):
    df['Date'] = pd.to_datetime(df['TransactionDate'])
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    summary_df = pd.DataFrame(df)
    group_by_y_m = summary_df.groupby(['Month', 'Year'])['Revenue'].sum().reset_index()
    new_index = group_by_y_m.set_index(['Month','Year'])
    return new_index
result = analyze_monthly_revenue(df_time_series)
print(result)
