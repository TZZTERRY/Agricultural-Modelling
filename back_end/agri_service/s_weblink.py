import json


class SWeblink:

    def __get_data_from_db(self):
        """
        Getting the data from database
        :return: None
        """

        # a sample data, in Json format.
        sample_data_js = """
               {
                    "websites":[
                        {
                            "title":"Weather",
                            "outline": "Bureau of Meterology",
                            "description":"Rainfall, Temperature, Wind, Humidity, Evaporation, Sunshine, Cyclones, Bushfires",
                            "url": "http://www.bom.gov.au/climate/change/index.shtml#tabs=Tracker&tracker=timeseries"
                     
                        },
                        {
                            "title":"Local Value",
                            "outline": "Australian Bureau of Statistics",
                            "description":"Contains final estimates of gross and local values of production of major agricultural commodities for Australia, states and territories",
                            "url": "http://www.bom.gov.au/climate/change/index.shtml#tabs=Tracker&tracker=timeseries"
                        
                        }   
                    ]
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
