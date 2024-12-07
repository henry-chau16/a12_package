import pandas as pd

def column_mean(col: pd.Series):
    try:
     return col.mean()
    except Exception as e:
       return False

def column_median(col: pd.Series):
    try:
        return col.median()
    except Exception as e:
       return False