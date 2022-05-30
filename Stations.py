class Station:

    def __init__(self, name):
        self.name = name
        self.connections = {}
        #self.__trains = []

    def add_connection(self, station, distance=0):
        self.connections[station] = distance

    def get_connections(self):
        return list(self.connections.keys())

    #@property
    #def trains(self):
        #return self.__trains

    #@trains.setter
    #def trains(self, train):
        #self.__trains.append(train)
