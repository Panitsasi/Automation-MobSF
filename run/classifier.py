import pandas as pd
import numpy as np
import config
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from pymongo import MongoClient
from config import PERMISSION_LIST
from mongodb import MONGODB
import csv

PERMISSION_LIST_NO_CLASS=[]
for item in range(len(PERMISSION_LIST)-1):
    PERMISSION_LIST_NO_CLASS.append(item)

temp = []

database = MONGODB(config.CONNECTION_STRING_MONGODB_DATABASE_LOCAL,"MobSF","LOCAL")

try:
    permission_apps_data = list(database.get_records_static().find({},{'permissions':1,'_id': 0}))
    app_names = list(database.get_records_static().find({},{'app_name':1,'_id': 0}))
    print('Data were successfully accessed.')
except:
    print('An error occurred while accessing the application data.')

database.close_connection()

current_app_permissions_json=permission_apps_data[-1]
current_app_name = app_names[-1]

for i in range(len(PERMISSION_LIST) -1 ):
    temp.append(0)

for elem in current_app_permissions_json['permissions']:
    try:
        index = PERMISSION_LIST.index(elem)
        if (index):
            temp[index] = 1

    except ValueError:
        pass


flags=tuple(temp)

with open("predict.csv", "wt") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(PERMISSION_LIST_NO_CLASS)
    writer.writerows([flags])
    fp.close()


data = pd.read_csv('Android_permissions_dataset.csv')

prediction = pd.read_csv("predict.csv")

df = pd.DataFrame(data, columns=data.columns)

df1 = pd.DataFrame(prediction, columns=data.columns)

X = df.drop(['CLASS'], axis='columns')

Y = data['CLASS']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)


# param_grid = {'C': [0.001,0.01,0.1, 1, 10, 100],
#                'gamma': [0.001,0.01,0.1, 1, 10, 100, 1000],
#                #'degree':[1,2,3,4,5],
#               'kernel': ['rbf']}

# grid = GridSearchCV(SVC(), param_grid, refit = True, verbose = 3 )

# # fitting the model for grid search
# grid.fit(X_train,Y_train)

# # print best parameter after tuning
# print(grid.best_params_)

# # print how our model looks after hyper-parameter tuning
# print(grid.best_estimator_)


model = SVC(C=10 , kernel='rbf', gamma = 0.001)

print('Algorithm training began...')

model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)

typeSample= model.predict(prediction)[0]

print('Application classification has started...')

if(typeSample):
    print('Classsified as Malware Sample.')
    database.insert_malware(current_app_name)

else:
    print('Classified as Benign Sample.')
    database.insert_benign(current_app_name)
































