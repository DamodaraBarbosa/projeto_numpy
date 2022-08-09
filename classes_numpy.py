import collections
import numpy as np
from utils.functions import linha, linha2

class Catalog:
    def __init__(self, array_strings, array_numbers) -> None:
        self.strings = array_strings
        self.numbers = array_numbers
            
    def num_artistis(self):
        name_of_artists = self.strings[0]
        return f'There are {len(name_of_artists)} artists on the plataform.'
    
    def sum_fans(self):
        number_of_fans = self.numbers[0]
        return f'There are {int(number_of_fans.sum())} fans on the plataform.'
    
    def sum_likes(self):
        number_of_likes = self.numbers[1]
        return f'There are {int(number_of_likes.sum())} likes on the plataform.'
    
    def sum_artists_cash(self):
        number_of_cash = self.numbers[2]
        return f'USD {number_of_cash.sum():.2f} was raised.'

    def mean_likes(self):
        return f'The average number of likes on the platform is {self.numbers[1].mean()} likes.'
    
    def mean_fans(self):
        return f'The average number of fans on the platform is {self.numbers[0].mean()} fans.'
    
    def mean_cash(self):
        return f'The average of fundraising was USD {self.numbers[2].mean():.2f}.'
    
    
    @staticmethod
    def mean_menu():
        pass