#!/usr/bin/env python
# coding: utf-8

# In[87]:


import numpy as np
import json
import pickle
from sklearn.compose import ColumnTransformer
import xgboost as xgb
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


# In[88]:


with open('col_transf.pkl','br') as ct:
    col_transf = pickle.load(ct)
with open('xgb.pkl','rb') as xg:
    xgb_trained = pickle.load(xg)


# In[90]:


import json
#  подаю следующие поля:
'''
rooms        - кол-во комнат (5 означет 5 и более)
area_tot     - общая площадь
area_kitchen - площадь кухни
floor        - этаж
floor_tot    - кол-во этажей
district     - район ('ленинский':0, 'орджоникидзевский':1, 'правобережный':2)
'''
dict1 = {'rooms':1,
         'area_tot':31,
         'area_kitchen':7,
         'floor':5,
         'floor_tot':7,
         'district':0}


# In[91]:


class Predict(Resource):
    def xgb_predict(self, input_dict):
#         input_dict = json.loads(input_json)
        input_arr = [input_dict['rooms'], 
                     input_dict['area_tot'],
                     input_dict['area_kitchen'],
                     input_dict['floor'],
                     input_dict['floor_tot'],
                     input_dict['district']]
        input_processed = col_transf.transform(np.array(input_arr).reshape(1,-1))
        output_dict = input_dict.copy()
        output_dict['price'] = int(round(xgb_trained.predict(input_processed).item(),0))
#         output_json = json.dumps(output_dict)
        return output_dict
    
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('rooms', required=True, location='args', type=int,dest='rooms')  # add args
        parser.add_argument('area_tot', required=True, type=float, dest='area_tot')
        parser.add_argument('area_kitchen', required=True, type=float, dest='area_kitchen')
        parser.add_argument('floor', required=True, type=int, dest='floor')
        parser.add_argument('floor_tot', required=True, type=int, dest='floor_tot')
        parser.add_argument('district', required=True, type=int, dest='district')
        
        args = dict(parser.parse_args())  # parse arguments to dictionary
        try:
            output = self.xgb_predict(args)
            status = 200
        except ValueError:
            output = {'data':'Bad request'}
            status = 400
        return output, status  # return data and status


# In[92]:


app = Flask(__name__)
api = Api(app)
api.add_resource(Predict, '/predict')  # '/predict' is our entry point


# In[93]:


if __name__ == '__main__':
    app.run()  # run our Flask app


# In[ ]:




