from data_loading import data_loading

def data_analysis():
    data = data_loading()
    print(data)

    print("null values------------", data.isnull().sum())
    print("duplicate values---------", data.duplicated().sum())
    print("unique values-------------", data.nunique())
    # print("---------------",data.columns.to_list())

    return data

data_analysis()