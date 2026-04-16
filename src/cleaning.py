import numpy as np

def drop_bedroom_outliers(df, bedroom_threshold: int = 15):
    """
    Drop rows where the number of bedrooms is greater than the specified threshold.
    """
    data = df.copy() 
    data = data[data['bedrooms'] <= bedroom_threshold]
    return data

def recalculate_sqft_basement(df):
    """
    Recalculate the 'sqft_basement' column by subtracting 'sqft_above' from 'sqft_living'.
    """
    data = df.copy()
    data['sqft_basement'] = data['sqft_living'] - data['sqft_above']
    return data

def fill_na_with_most_common_value(df, column_names: list = ['waterfront', 'view']):
    """
    Fill NA values in the specified columns with the most common value (mode) of each column.
    """
    data = df.copy()
    for col in column_names:
        most_common_value = data[col].mode()[0]
        data[col].fillna(most_common_value, inplace = True)
    return data

def last_known_change(df):
    """
    Create a new column 'last_known_change' that indicates the last known change in the property.
    If 'yr_renovated' is not 0, use that value; otherwise, use 'yr_built'.
    """
    data = df.copy()
    data['yr_renovated'] = data['yr_renovated'].replace(0, np.nan)
    data['last_known_change'] = data['yr_renovated'].fillna(data['yr_built'])
    return data

def drop_columns(df, columns_to_drop: list = ['yr_renovated', 'yr_built']):
    """
    Drop the specified columns from the DataFrame.
    """
    data = df.copy()
    data.drop(columns=columns_to_drop, inplace=True)
    return data
