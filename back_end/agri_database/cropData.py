class crop_Data(object):
    def __init__(self, name, years, values, regionname):
        self.__name = name
        self.__years = years
        self.__values = values
        self.__regionname = regionname

        @property
        def name(self):
            return self.__name

        @property
        def years(self):
            return self.__years

        @property
        def values(self):
            return self.__values

        @property
        def regionname(self):
            return self.__regionname
        '''
        @years.setter
        def values(self, value):
            self.__values = value
            return self.__values
        '''







