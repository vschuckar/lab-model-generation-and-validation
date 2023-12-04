
import pandas as pd

def label_lower(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function formats the column names of the receive pd.DataFrame to lowercase letters.
    '''
    labels = []
    for column in df.columns:
        labels.append(column.lower())
    df.columns = labels
    return df

def to_int(df: pd.DataFrame, columns_to_int: list) -> pd.DataFrame:
    '''
    This function first rounds the decimals of numbers in the columns from a determined given list of columns in a pd.DataFrame then transforms it from their numeric type to an integer.
    '''
    df_copy = df.copy()
    for column in columns_to_int:
        df_copy[column] = df_copy[column].round().astype(int)
    return df_copy

def nan_values(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function creates a pd.DataFrame which shows the percentage of NaN or null values for all the columns in the provided pd.DataFrame.
    '''
    missing_values_df = pd.DataFrame(round(df.isna().sum()/len(df),4)*100) 
    missing_values_df = missing_values_df.reset_index() # replace, reset index and become columns
    missing_values_df.columns = ['column_name', 'percentage_of_missing_values'] # rename columns
    return missing_values_df


def column_rename(df: pd.DataFrame, column = None) -> pd.DataFrame:
    '''
    Function for renaming columns.
    '''
    if column is not None:
        df = df.rename(columns=column)
    return df

def to_num(df: pd.DataFrame, columns_to_num: list) -> pd.DataFrame:
    '''
    This function transforms your dtype into integer in determined column(s).
    '''
    df_copy = df.copy()
    for column in columns_to_num:
        df_copy[column] =  pd.to_numeric(df_copy[column], errors = 'coerce')
    return df_copy

def to_round(df: pd.DataFrame, columns_to_round: list) -> pd.DataFrame:
    '''
    This function rounds your float number in determined column(s). 
    '''
    df_copy = df.copy()
    for column in columns_to_round:
        df_copy[column] =  df_copy[column].round(2)
    return df_copy

def all_gone(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function drops all the rows for which all columns are also NaN.
    '''
    df_copy = df.copy()
    df_copy = df_copy.dropna(how = 'all', subset = df.columns)
    return df_copy 

def clean_gender_column(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function will take a Pandas DataFrame as an input and it will replace the values in
    the "gender" column ins such a way that any gender which is not Male or Female with be 
    replaced by "U" otherwise the genders will be either "F" or "M"

    Inputs:
    df: Pandas DataFrame

    Outputs:
    A pandas DataFrame with the values in the "gender" column cleaned.
    '''

    df2 = df.copy()

    if "gender" not in df2.columns:
        return df2
    else:
        #df2['gender'] = df2['gender'].apply(lambda x: x[0].upper() if x[0].upper() in ['M', 'F'] else "U")
        df2['gender'] = list(map(lambda x: x[0].upper() if x[0].upper() in ['M', 'F'] else "U", df2['gender']))
        return df2

def to_median_na(df: pd.DataFrame, columns_to_median: list) -> pd.DataFrame:
    '''
    This function adds the median values of a column to the NaN values of it. 
    '''
    df_copy = df.copy()
    for column in columns_to_median:
        median_value = df_copy[column].median()
        df_copy[column] = df_copy[column].fillna(median_value)
    return df_copy

def drop_column(df: pd.DataFrame):
    '''
    This function creates a copy of the original df and drops a specific column if it exists
    in a Pandas data frame.

    Inputs:
    df: pd.DataFrame

    Output:
    Copy of the original df without the specific column
    '''
   
    df2 = df.copy()
    if 'Unnamed: 0' in df2.columns: 
        df2 = df2.drop('Unnamed: 0', axis = 1) 
    return df2