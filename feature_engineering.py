from data_cleaning import data_cleaning
from sklearn import preprocessing

def feat_eng():
    data = data_cleaning()
    print(data)
    label_encoder = preprocessing.LabelEncoder()
    object_columns = data.select_dtypes(include=['object']).columns
    print("object_columns----------------", object_columns)
    num = []
    obj = []
    for col in data.columns:
        if data[col].dtype == "object":
            obj.append(col)
        else:
            num.append(col)

    print("num-----------------", num)
    print("obj-----------------", obj)

    for col in obj:
        data[col] = label_encoder.fit_transform(data[col])

    data.to_csv("bank_interest_rate.csv")

    return data
feat_eng()