import json
import pickle
import numpy as np
import os

# Create global variables
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower()) #if we cant find index this throws an error
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1 # the remaining elements will be 0 due to 1 hot encoding
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __locations
    global __data_columns
    global __model

    with open(os.getcwd()+"/server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns'] # interpreted as dictionary
        __locations = __data_columns[3:]
    with open(os.getcwd()+'/server/artifacts/banglore_home_prices_model.pickle', 'rb') as f: # b: binary model
        __model = pickle.load(f)
    print('loading saved artifact..done')

load_saved_artifacts()
#    print(get_location_names())
#    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
#    print(get_estimated_price('1st Phase JP Nagar',1000, 2, 2))