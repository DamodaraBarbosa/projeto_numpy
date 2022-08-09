from classes_numpy import Catalog
import numpy as np
import collections
from utils.functions import linha, linha2, menu_ranking_fans

class Analysis(Catalog):
    def __init__(self, strings, numbers ) -> None:
        super().__init__(strings, numbers)

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

        linha()
        print(f'{"Gênero musical":<35}', end='')
        print('Nº de artistas')
        linha()

        for key, value in count_musical_style.items():
            print(f'{key:<40}', end=' ')
            print(value)
            print('\033[1;33m--\033[m'*28)
        
    def ranking_artists_fans(self):
        #argsort indica os indexs dos elementos em ordem do array
        number_of_fans = self.numbers[0]
        name_of_artists = self.strings[0]
        index_ranking_fans = np.argsort(self.numbers[0])
        sorted_fans = number_of_fans[index_ranking_fans]
        sorted_artists_fans = name_of_artists[index_ranking_fans]
        ranking_fans = np.array([sorted_artists_fans, sorted_fans])
        ranking_fans_stacked = np.column_stack(ranking_fans)

        menu_ranking_fans()

        for cont in range(-1, -11, -1):
            print(f'{-cont}', end='')
            print(f'{"º":<10}', end='')
            print(f'\t{ranking_fans_stacked[cont, 0]:<20}', end='')
            print(f'\t{ranking_fans_stacked[cont, 1]}')
            if cont == -10:
                pass
            else:
                linha()
        linha2()
