import numbers


import numpy as np

class Catalog:
    def __init__(self, strings, numbers) -> None:
        self.strings = strings
        self.numbers = numbers

    def mean_likes(self):
        return f'{self.numbers[1].mean()} likes.'
    
    def mean_fans(self):
        return f'{self.numbers[0].mean()} fans.'