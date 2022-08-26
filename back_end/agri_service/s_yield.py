import json


class SYield:

    def __get_data_from_db(self):
        """
        Getting the data from database
        :return: None
        """

        # a sample data, in Json format.
        sample_data_js = """
                {
                    "years":[2023, 2024, 2025],
                    "values":[3420, 2002, 3400, 3000],
                    "crop name":"wheat",
                    "crop id":1,
                    "isPredict":true,
                    "regionName":"QID"
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
