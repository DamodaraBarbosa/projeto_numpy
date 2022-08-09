import collections
import numpy as np
from utils.functions import linha, linha2

class Catalog:
    def __init__(self, strings, numbers) -> None:
        self.strings = strings
        self.numbers = numbers
        self.conversion = 0
    
    def num_artistis(self):
        return f'São ao todo {len(self.strings[0])} artistas na plataforma.'
    
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
    
    
    @staticmethod
    def mean_menu():
        pass