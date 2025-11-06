
import gzip
import json
import pickle

import pandas as pd



def wrangle(filename):
    with gzip.open(filename,"r") as f:
        dataset=json.load(f)
    df=pd.DataFrame().from_dict(dataset["data"]).set_index("company_id")
    return df



def make_predictions(data_filepath, model_filepath):

    X_test = wrangle(data_filepath)

    with open(model_filepath,"rb") as f:
        model= pickle.load(f)

    y_test_pred = model.predict(X_test)

    y_test_pred = pd.Series(y_test_pred,index=X_test.index,name="bankrupt")
    return y_test_pred
