import numpy as np
from utils.ranking_analysis import Analysis

names = np.loadtxt('nome_catalogo.txt', dtype=str)
musical_style = np.loadtxt('genero_catalogo.txt', dtype=str)
solo_band_duo = np.loadtxt('tipo_catalogo.txt', dtype=str)
fans = np.loadtxt('fans_catalogo.txt', dtype=int)
likes = np.loadtxt('curtidas_catalogo.txt', dtype=int)
cash = np.loadtxt('faturament_catalogo.txt')

catalog_strings = np.column_stack([names, musical_style, solo_band_duo])
catalog_numbers = np.column_stack([fans, likes, cash])
catalog_analysis = Analysis(catalog_strings, catalog_numbers)

catalog_analysis.artists_ranking_conv_fanslikes()


# catalog_analysis.fans_likes_conversion()
# print(catalog_analysis.artist_ranking_conversion())
# complete_catalog.fans_likes_conversion()
# print(complete_catalog.artist_biggest_conversion())
