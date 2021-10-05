import pandas as pd
import re

def wrangle_with_dt(filepath):
    """
    Wrangle function takes an input of a filepath which contains a date-time,
    outputs a cleaned dataframe
    """
    # Reads in DF from filepath using Pandas
    df = pd.read_csv(filepath, parse_dates=['Fiscal Year Start', 'Fiscal Year End'])
    
    # Seperates the categorical columns
    categorical_cols = df.select_dtypes('object').columns
    
    #Creates threshold for how many times you will allow the same value to show up in multiple columns in a row.
    threshold = 50
    
    #Identify high cardinality columns
    high_card_cols = [col for col in categorical_cols 
                      if df[col].nunique() > threshold]
    
    # Drop high cardinality columns
    df.drop(high_card_cols, axis=1, inplace=True)
    
    # Drop columns with a high number of NaN values
    if len(df) > 100:
        df = df.dropna(axis = 1, thresh = 100)
    # Fill NA values with front fill. Replaces with value ahead of it.
    df = df.fillna(method='ffill')
    df = df.fillna(method='bfill')
    
    # Clear punctuation/special characters from columns using regex
    punct_regex = r"[^0-9a-zA-Z\s]"
    special_char_regex = r'[\$\%\&\@+\"\'\,]'
    df.columns = df.columns.str.replace('[?]', '')
    df.columns = df.columns.str.replace(r'[/,\\]', ' ')
    # Lambda apply regex to df
    df = df.rename(columns = lambda x: 
        re.sub(punct_regex, "", x))
    df = df.rename(columns = lambda x:
        re.sub(special_char_regex, "", x))
    
    # Replace all spaces with an underscore for proper formatting
    df = df.rename(columns = lambda x:
        x.replace(" ", "_"))
    
    # Case normalize column names
    df.columns = df.columns.str.lower()
    
    return df

def wrangle_without_dt(filepath):
    """
    Wrangle function takes an input of a filepath which does not contains a date-time,
    outputs a cleaned dataframe
    """
    # Reads in DF from filepath using Pandas
    df = pd.read_csv(filepath)
    
    # Seperates the categorical columns
    categorical_cols = df.select_dtypes('object').columns
    
    #Creates threshold for how many times you will allow the same value to show up in multiple columns in a row.
    threshold = 50
    
    #Identify high cardinality columns
    high_card_cols = [col for col in categorical_cols 
                      if df[col].nunique() > threshold]
    
    # Drop high cardinality columns
    df = df.drop(high_card_cols, axis=1)
    
    # Drop columns with a high number of NaN values
    if len(df) > 100:
        df = df.dropna(axis = 1, thresh = 100)
    # Fill NA values with front fill. Replaces with value ahead of it.
    # Replaces values at start of data with last 
    df = df.fillna(method='ffill')
    df = df.fillna(method='bfill')
    
    # Clear punctuation/special characters from columns using regex
    punct_regex = r"[^0-9a-zA-Z\s]"
    #special_char_regex = r'[\$\%\&\@+\"\'\,]'
    df.columns = df.columns.str.replace('[?]', '')
    df.columns = df.columns.str.replace(r'[/,\\]', ' ')
    # Lambda apply regex to df
    df = df.rename(columns = lambda x: 
        re.sub(punct_regex, "", x))
    #df = df.rename(columns = lambda x:
       # re.sub(special_char_regex, "", x))
    
    # Replace all spaces with an underscore for proper formatting
    df = df.rename(columns = lambda x:
        x.replace(" ", "_"))
    
    # Case normalize column names
    df.columns = df.columns.str.lower()
    
    return df