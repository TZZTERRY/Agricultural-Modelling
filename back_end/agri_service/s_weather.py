import json


class SWeather:

    def __get_data_from_db(self):
        """
        Getting the data from database
        :return: None
        """

        # a sample data, in Json format.
        sample_data_js = """
                {
                    "years":[1999, 2000, 2000, 2021],
                    "values":[34, 22, 34, 30],
                    "regionName":"QID",
                    "data type:":"temperature"
                }
                """

        self.__data_object = json.loads(sample_data_js)  # transfer Json into python object

    def get_data(self):
        """
        Pass the data
        :return:
        """
        self.__get_data_from_db()  # update the data
        return json.dumps(self.__data_object)
