import json
import os
import config
from datetime import datetime

class Converter:

    def __init__(self,path,filename):

        self.__path=path   #Path to current folder run
        self.__filename=filename #Name of static_data.txt
        self.__json_data={}


    def get_path(self):
        return self.__path

    def get_filename(self):
        return self.__filename

    def get_json_data(self):
        return self.__json_data

    def set_path(self,path):
        self.__path=path

    def set_filename(self, filename):
        self.__filename = filename

    def set_json_data(self, json_data):
        self.__json_data = json_data

    def add_json_data(self,key,value):
        self.__json_data[key]=value

    def convert_to_json(self):

          try:
            with open(os.path.join(self.__path, self.__filename)) as file:
                data = file.read()
                data= json.loads(data)
                json_format = json.dumps(data, indent=2, sort_keys=True)
                for i in data:
                    if i in config.STATIC_ANALYSIS_DATA_TYPE:
                        self.__json_data[i] = data[i]

                self.__json_data['day']= datetime.now().strftime("%d-%m-%Y")
                self.__json_data['time'] = datetime.now().strftime("%H:%M:%S")
                permissions_dict = self.__json_data['permissions']
                permissions=[]

                for key in permissions_dict.keys():
                    if(key.split('.')[0]=='android'):
                     permissions.append(key.split('.')[-1])
                    else:
                        continue
                self.__json_data['permissions']=permissions

            return self.__json_data

          except:
              print('An error occurred while accessing the file')


