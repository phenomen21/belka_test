# belka_test
This is a data science test task for the software company named Belka Digital

The task was as follows:
1. Build the ML model predicting the price of a given apartment in the city of Magnitogorsk, Russia 
(get data from the www.citystar.ru website)
3. The model must be implemented as RESTful API, with JSON in input and JSON in output
4. If this task will be implemented in a docker image building from the reposotory that would be a plus

I used Flask-restful to build the RESTful API

Files:
* /EDA/EDA_Belka_RUS.ipynb - EDA and building of the ML model (in Russian)
* /EDA/EDA_Belka_ENG.ipynb - EDA and building of the ML model (in English)
* /EDA/CityStarExport.xls - Excel document containing the main data from the www.citystar.ru website (downloaded Jun 7 2022)
* /EDA/Magn_streets.xlsx - Excel documents (3 sheets) with "street" - "district" mapping (composed from data downloaded from https://youkarta.ru/cheljabinskaja-obl/magnitogorsk-74/)
* API_main.py - API code
* col_transf.pkl - Pickle serialized saved sklearn.compose.ColumnTransformer object for one-hot encoding
* xgb_trained - trained XGBoost model for prediction (saved with xgb.save_model)

Model requires numpy, pandas, flask, flask_restful, XGBoost and sklearn packages installed
