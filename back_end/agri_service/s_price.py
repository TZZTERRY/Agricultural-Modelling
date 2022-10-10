import json


class SPrice:

    def __get_data_from_db(self):
        """
        Getting the data from database
        :return: None
        """

        # a sample data, in Json format.
        sample_data_js = """
                {
                    "data": [["1990",148687],["1991",73990],["1992",161567],["1993",132749],["1994",122648],["1995",203522],["1996",199938],["1997",166463],["1998",175096],["1999",183729],["2000",192362],["2001",200995],["2002",209628],["2003",247625],["2004",168917],["2005",144572],["2006",142900],["2007",218211],["2008",333256],["2009",237919],["2010",193858],["2011",215190],["2012",162825],["2013",284260],["2014",259454],["2015",267102],["2016",242558],["2017",202513],["2018",262908],["2019",377268],["2020",338366]],
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
