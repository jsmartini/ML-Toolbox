import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer

    #creates a onehot encoding of each series in the series lists. creates dummy series, concats and drops the initial series from df
    #wrote this because pd.get_dummies would run out of memory in my jupyter instance, sklearn does it much more efficiently

def onehot(df:pd.DataFrame, series_list:list):
    encoder = LabelBinarizer()
    transformed = []
    df.dropna()
    for series in series_list:
        #print("Starting {}".format(series))
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
            df.drop(series, axis=1, inplace=True)
            print("TypeError on Series {0}, Dropping and Skipping".format(series))
    #print(transformed)
    transformed.append(df)
    return pd.concat(transformed, axis=1)  