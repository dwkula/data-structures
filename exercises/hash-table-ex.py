"""
1. nyc_weather.csv contains new york city weather for first few days in the month of January. 
Write a program that can answer following,
        1. What was the average temperature in first week of Jan
        2. What was the maximum temperature in first 10 days of Jan

Figure out data structure that is best for this problem


2. nyc_weather.csv contains new york city weather for first few days in the month of January. 
Write a program that can answer following,
       1. What was the temperature on Jan 9?
       2. What was the temperature on Jan 4?

Figure out data structure that is best for this problem
"""


import sys
weather_data_list = []
weather_data_dict = {}


with open(sys.path[0] + "/files-for-exercises/nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temperature = int(tokens[1])
        weather_data_list.append([day, temperature])


def ex1_1():
    temp = 0
    for i in range(7):
        temp += weather_data_list[i][1]
    return temp/7


def ex1_2():
    first_ten_days = []
    for i in range(10):
        first_ten_days.append(weather_data_list[i][1])
    return max(first_ten_days)


with open(sys.path[0] + "/files-for-exercises/nyc_weather.csv", "r") as fi:
    for line in fi:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_data_dict[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")


def ex2_1():
    return weather_data_dict['Jan 9']


def ex2_1():
    return weather_data_dict['Jan 4']


words_count = {}
with open(sys.path[0] + "/files-for-exercises/poem.txt", "r") as fil:
    for line in fil:
        words = line.split(' ')
        for word in words:
            word = word.replace('\n', '')
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1


"""
Implement hash table where collisions are handled using linear probing. 
We learnt about linear probing in the video tutorial. Take the hash table implementation that
uses chaining and modify methods to use linear probing. Keep MAX size of arr in hashtable as 10.

"""


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if None not in self.arr:
            raise Exception("Hash map is full")

        if self.arr[h] == None or self.arr[h][0] == key:
            self.arr[h] = (key, val)
        else:
            if h < len(self.arr) - 1:
                for index, element in enumerate(self.arr[h:]):
                    new_h = h + index
                    if element is None:
                        self.arr[new_h] = (key, val)
                        break
            else:
                for index, element in enumerate(self.arr):
                    if element is None:
                        self.arr[index] = (key, val)
                        break

    def __getitem__(self, key):
        pass

    def __delitem__(self, key):
        pass
