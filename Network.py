from Stations import Station
from random import randint
from Train import Train
import shelve
import time


class Network:

    def __init__(self):
        self.stations = {}


    def add_station(self, station_name):
        new_station = Station(station_name)
        self.stations[new_station.name] = new_station
        

    def add_station_connection(self, from_station_name, to_station_name, distance):
        self.stations[from_station_name].add_connection(self.stations[to_station_name], distance)

    def return_stations(self):
        return list(self.stations.keys())
    
    def __string_to_object(self, string):
        for i in self.stations:
            if i == string:
                return self.stations[i]



    def get_path(self, current, target, visited = None, stack = None):
        if isinstance(current, str):
            current = self.__string_to_object(current)

        if isinstance(target, str):
            target = self.__string_to_object(target)

        if not visited:
            visited = []
        
        if not stack:
            stack = [current]

        visited.append(current)

        if current == target:
            return [i.name for i in stack]

        for i in current.get_connections():
            if i not in visited:
                stack.append(i)
                path = self.get_path(i, target, visited, stack)
                if path:
                    return path
                else:
                    stack.pop()
    


    
    def simulate(self):
        current_train = Train()
        print("Which path will this train take? (Pick 2 stations)")
        available = self.return_stations()
        print(available)
        name1 = input()
        name2 = input()

        if name1 not in available:
            print("That station does not exist!")
            return
        
        if name2 not in available:
            print("That station does not exist!")
            return

        if name1 == name2:
                print("The train is already here!")
                time.sleep(3)
                return
        
        path = self.get_path(name1, name2)
       
        
        for i in range(len(path) - 1):
            print(f"The train is at {path[i]}!\n")
            entered = randint(0, current_train.get_capacity() - current_train.get_passengers())
            exited = randint(0, current_train.get_passengers())
            print(f'{exited} passengers exited the train!')
            print(f'{entered} passengers entered the train!\n')
            current_train.add_passengers(-1 * exited)
            current_train.add_passengers(entered)
            print(f"The train is heading to {path[i + 1]}!\n")
            time.sleep(3)
            
        print(f"The train is at {path[-1]}!")
        print("The train is at it's final stop!")  
        print(f'{current_train.get_passengers()} passengers exited the train!')
        current_train = None
    


    def dump(self):
        with shelve.open('storage.db') as storage:
            station_names = [i for i in self.stations.keys()]
            storage['names'] = station_names

            station_connections = {}
            for i in self.stations.values():
                station_connections[i.name] = {i.name:0 for i in i.connections.keys()}
            
            storage['connections'] = station_connections
       
    def load(self):
        with shelve.open('storage.db') as storage:
            for i in storage['names']:
                new_station = Station(i)
                self.stations[new_station.name] = new_station
            
            for i in storage['connections']: 
               for j in storage['connections'][i]:
                    self.stations[i].add_connection(self.stations[j], 0)



            
            storage.clear()