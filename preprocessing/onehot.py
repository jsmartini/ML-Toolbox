import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer

def onehot(df:pd.DataFrame, series_list:list):
    #creates a onehot encoding of each series in the series lists. creates dummy series, concats and drops the initial series from df
    #wrote this because pd.get_dummies would run out of memory in my pandas only onehot function, sklearn does it much more efficiently
    encoder = LabelBinarizer()
    transformed = []
    df.dropna()
    for series in series_list:
        print("Starting {}".format(series))
        x = df[series]
        try:
            encoder = LabelBinarizer()
            encoder.fit(x.to_numpy())
            transform = pd.DataFrame(encoder.transform(x.to_numpy()))
            #print(transform.head(10))
            transform = transform.add_prefix(series)
            #print(transform.head(5))
            transformed.append(transform)
            df.drop(series, axis=1, inplace=True)
        except TypeError:
            #the lazy way out
            df.drop(series, axis=1, inplace=True)
            print("TypeError on Series, Dropping and Skipping")
    #print(transformed)
    transformed.append(df)
    return pd.concat(transformed)