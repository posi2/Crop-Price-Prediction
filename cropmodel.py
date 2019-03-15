import numpy as np
import keras
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

K.clear_session()

def prediction(input_value):
    
    input_list=[]
    input_list.append(input_value['Year'])
    input_list.append(input_value['Month'])
    input_list.append(89) #rainfall value
    if(input_value['District']=="Indore"):
        input_list.append(1)
        input_list.append(0)
    if(input_value['District']=="Jabalpur"):
        input_list.append(0)
        input_list.append(1)
    
    
    input_list = np.array(input_list)
    input_list = input_list.reshape( (1,5) )
    input_list = np.matrix(input_list)

    json_file = open('/home/posi2/Data-Science/crop-price-prediction-hackathon/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    global graph
    graph=tf.get_default_graph()

    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("/home/posi2/Data-Science/crop-price-prediction-hackathon/model.h5")
    with graph.as_default():
        loaded_model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])

        values=loaded_model.predict(input_list)
        del input_list
    keras.backend.clear_session()
    return values
