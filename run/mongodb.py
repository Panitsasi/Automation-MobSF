from pymongo import MongoClient

class MONGODB:

    def __init__(self, url, name,type):

        self.__url = url
        self.__name = name
        self.type=type
        self.__client=None
        self.__records_static=None
        self.__records_dynamic=None
        self.__records_malware= None
        self.__records_benign = None
        try:
            self.__client = MongoClient(self.__url)
            self.__db = self.__client.get_database(self.__name)
            print('Connect to '+ self.type + ' database...')
            self.__records_static = self.__db.static_data
            self.__records_dynamic = self.__db.dynamic_data
            self.__records_malware = self.__db.malware
            self.__records_benign = self.__db.benign

        except:
            print('An error occurred while connecting to the database')

    def get_url(self):
        return self.__url

    def get_name(self):
        return self.__name

    def get_client(self):
        return self.__client

    def get_records_static(self):
        return self.__records_static

    def get_records_dynamic(self):
        return self.__records_dynamic

    def get_records_malware(self):
        return self.__records_malware

    def get_records_benign(self):
        return self.__records_benign

    def set_url(self,url):
        self.__url= url

    def set_name(self, name):
        self.__name = name

    def set_client(self,client):
        self.__client=client

    def set_records_static(self,records_static):
        self.__records_static=records_static

    def set_records_dynamic(self, records_dynamic):
        self.__records_dynamic = records_dynamic

    def close_connection(self):
        self.__client.close()
        print('Closed the connection to '+ self.type + ' database.')

    def insert_static_data(self,json_data):

        try:
            self.__records_static.insert_one(json_data)
            print('Data inserted.')
        except:
            print('An error occured while inserting data to database.')

    def insert_dynamic_data(self, json_data):

        try:
            self.__records_dynamic.insert_one(json_data)
            print('Data inserted.')

        except:
            print('An error occured while inserting data to database.')

    def insert_malware(self, json_data):

        try:
            self.__records_malware.insert_one(json_data)
            print('Data inserted.')
        except:
            print('An error occured while inserting data to database.')

    def insert_benign(self, json_data):

        try:
            self.__records_benign.insert_one(json_data)
            print('Data inserted.')
        except:
            print('An error occured while inserting data to database.')

    def delete_static_data_collection(self):

        try:
            self.__records_static.drop()
            print('Data deleted.')
        except:
            print('An error occured while deleting data to database.')

    def delete_dynamic_data_collection(self):

        try:
            self.__records_dynamic.drop()
            print('Data deleted.')
        except:
            print('An error occured while deleting data to database.')

    def permissionApp(self):
        return self.__records_static

    def __str__(self):
        return 'Database name: '+ self.__name + '  ' + 'Connection String: '+ self.__url

