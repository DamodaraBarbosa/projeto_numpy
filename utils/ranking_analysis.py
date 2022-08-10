from classes_numpy import Catalog
import numpy as np
import collections
from utils.functions import linha, linha2, menu_ranking_cash, menu_ranking_conversion, menu_ranking_fans, menu_ranking_likes

class Analysis(Catalog):
    def __init__(self, strings, numbers ) -> None:
        super().__init__(strings, numbers)
        self.conversion = 0

    def artist_ranking_conversion(self):
        #self.numbers[:, 1] equivale ao nº de curtidas e self.numbers[:, 0] ao nº de fãs
        self.conversion = (self.numbers[:, 1]/self.numbers[:, 0]) * 100
        index_ranking_conversion = np.argsort(self.conversion)
        # o uso de [index_ranking_conversion] ordena o nome dos artistas com maior conversão de fãs em likes
        name_of_artists = self.strings[:, 0][index_ranking_conversion]
        # o uso de [index_ranking_conversion] deixa a conversão de fãs em likes em ordem crescente
        conversion_fans_likes = self.conversion[index_ranking_conversion]
        ranking_conversion_1D = np.array([name_of_artists, conversion_fans_likes])
        ranking_conversion_2D = np.column_stack(ranking_conversion_1D)

        menu_ranking_conversion()

        for cont in range(-1, -11, -1):
            print(f'{-cont}', end='')
            print(f'{"º":<10}', end='')
            print(f'{ranking_conversion_2D[cont, 0]}', end='')
            print(f'{ranking_conversion_2D[cont, 1]}')

    def ranking_artists_fans(self):
        #argsort indica os indexs dos elementos em ordem do array
        index_ranking_fans = np.argsort(self.numbers[:, 0])
        number_of_fans_sorted = self.numbers[:, 0][index_ranking_fans]
        name_of_artists = self.strings[:, 0][index_ranking_fans]
        ranking_fans = np.array([name_of_artists, number_of_fans_sorted])
        ranking_fans_stacked = np.column_stack(ranking_fans)

        menu_ranking_fans()

        for cont in range(-1, -11, -1):
            print(f'{- cont}', end='')
            print(f'{"º":<10}', end='')
            print(f'\t{ranking_fans_stacked[cont, 0]:<20}', end='')
            print(f'\t{ranking_fans_stacked[cont, 1]}')
            if cont == -10:
                pass
            else:
                linha()
        linha2()
    
    def ranking_artists_likes(self):
        index_ranking_likes = np.argsort(self.numbers[:, 1])
        name_of_artists = self.strings[:, 0][index_ranking_likes]
        number_of_likes_sorted = self.numbers[:, 1][index_ranking_likes]
        ranking_likes = np.array([name_of_artists, number_of_likes_sorted])
        ranking_likes_stacked = np.column_stack(ranking_likes)

        menu_ranking_likes()

        for cont in range(-1, -11, -1):
            print(f'{- cont}', end='')
            print(f'{"º":<10}', end='')
            print(f'\t{ranking_likes_stacked[cont, 0]:<22}', end='')
            print(f'\t{ranking_likes_stacked[cont, 1]}')
            if cont == -10:
                pass
            else:
                linha()
        linha2()
    
    def ranking_artists_cash(self):
        index_ranking_cash = np.argsort(self.numbers[:, 2])
        name_of_artist = self.strings[:, 0][index_ranking_cash]
        number_of_cash = self.numbers[:, 2][index_ranking_cash]
        ranking_cash = np.array([name_of_artist, number_of_cash])
        ranking_cash_stacked = np.column_stack(ranking_cash)

        menu_ranking_cash()

        for cont in range(-1, -11, -1):
            print(f'{- cont}', end='')
            print(f'{"º":<10}', end='')
            print(f'\t{ranking_cash_stacked[cont, 0]:<22}', end='')
            print(f'\t{ranking_cash_stacked[cont, 1]}')
            if cont == -10:
                pass
            else:
                linha()
        linha2()
