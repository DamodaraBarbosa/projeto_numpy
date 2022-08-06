import collections
import numpy as np

class Catalog:
    def __init__(self, strings, numbers) -> None:
        self.strings = strings
        self.numbers = numbers
        self.conversion = 0

    def mean_likes(self):
        return f'{self.numbers[1].mean()} likes.'
    
    def mean_fans(self):
        return f'{self.numbers[0].mean()} fans.'
    
    def mean_cash(self):
        return f'USD {self.numbers[2].mean():.2f}.'
    
    def fans_likes_conversion(self):
        self.conversion = (self.numbers[1]/self.numbers[0]) * 100
        return self.conversion

    def artist_biggest_conversion(self):
        artist_conversion = np.array([self.strings[0]])

    def count_musical_style(self):
        #contagem de elementos que se repetem em um array
        count_musical_style = collections.Counter(self.strings[1])
        return count_musical_style['MPB']
    
    @staticmethod
    def mean_menu():
        pass