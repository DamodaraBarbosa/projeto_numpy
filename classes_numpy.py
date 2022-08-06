import collections
import numpy as np

class Catalog:
    def __init__(self, strings, numbers) -> None:
        self.strings = strings
        self.numbers = numbers
        self.conversion = 0
    
    def sum_fans(self):
        return f'São ao todo {int(self.numbers[0].sum())} fãs na plataforma.'
    
    def sum_likes(self):
        return f'São ao todo {int(self.numbers[1].sum())} curtidas na plataforma.'
    
    def sum_artists_cash(self):
        return f'O faturamento dos artistas foi de USD {int(self.numbers[2].sum())}.'

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
        artist_conversion = np.column_stack([self.strings[0], self.conversion])
        #retorna o index do elemento dentro de um array no formato: (array([8], dtype=int64),)
        index_max_conversion = (np.where(self.conversion == max(self.conversion)))
        #retorna o número, o valor do index        
        print(index_max_conversion[0][0])
        
        return artist_conversion[index_max_conversion, 0]

    def count_musical_style(self):
        #contagem de elementos que se repetem em um array
        count_musical_style = collections.Counter(self.strings[1])
        return count_musical_style['MPB']
    
    def ranking_artists_fans(self):
        return np.sort(self.numbers[0])
    
    @staticmethod
    def mean_menu():
        pass