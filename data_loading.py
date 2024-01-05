import pandas as pd

def data_loading():
    df=pd.read_csv("loans_full_schema.csv")
    # print(df)
    return df

data_loading()