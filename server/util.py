import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqm, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqm
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1    
    
    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open("./artifacts/PH_Houses_Price_Prediction.pickle", "rb") as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("Alabang, Muntinlupa", 1, 1, 36))
    print(get_estimated_price("Bakakeng Central, Baguio", 2, 1, 50))
    print(get_estimated_price("Novaliches, Quezon City", 1, 1, 70))
    print(get_estimated_price("Sasa, Davao", 1, 1, 32))

