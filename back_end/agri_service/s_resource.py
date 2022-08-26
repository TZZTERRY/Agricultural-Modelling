import json


class SResource:

    def __get_data_from_db(self):
        """
        Getting the data from database
        :return: None
        """

        # a sample data, in Json format.
        sample_data_js = """
                sdfdfdfdfdvsdfsdefefasdasfdfdfasfasfasf
                """

        self.__data_object = json.loads(sample_data_js)  # transfer Json into python object

    def get_data(self):
        """
        Pass the data
        :return:
        """
        self.__get_data_from_db()  # update the data
        return json.dumps(self.__data_object)
