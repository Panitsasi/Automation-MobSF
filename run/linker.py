class Linker:

    def __init__(self,database,converter,data=None):
        self.__database=database
        self.__converter=converter
        self.__data=data

    def get_database(self):
        return self.__database

    def converter(self):
        return self.__converter

    def set_database(self,database):
        self.__database=database

    def converter(self,converter):
        self.__converter=converter

    def upload(self):
        self.__data=self.__converter.convert_to_json()
        self.__database.insert_static_data(self.__data)
        self.__database.close_connection()



