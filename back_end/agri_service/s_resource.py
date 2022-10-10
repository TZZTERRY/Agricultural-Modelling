import json
import os
from flask import send_from_directory

class SResource:
    __image_resource__ = "image_resource/"
    IMAGE_NUM = 1

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

    def get_data(self, file_name, type_num, file_format):
        """
        Pass the data
        :return:
        """
        if type_num == self.IMAGE_NUM:  # is a image format
            file_path = self.__image_resource__ + file_name + "." + file_format
            if not os.path.exists(file_path):  # file not exist:
                raise Exception("Request image file: [" + file_name + "] is not in path: " + file_path)

            return send_from_directory("", file_path)

        raise Exception("Unknown file type: "+str(type_num))
