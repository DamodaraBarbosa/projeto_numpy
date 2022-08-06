import numpy as np
from classes_numpy import Catalog

names = np.loadtxt('nome_catalogo.txt', dtype=str)
musical_style = np.loadtxt('genero_catalogo.txt', dtype=str)
solo_band_duo = np.loadtxt('tipo_catalogo.txt', dtype=str)
fans = np.loadtxt('fans_catalogo.txt', dtype=int)
likes = np.loadtxt('curtidas_catalogo.txt', dtype=int)
cash = np.loadtxt('faturament_catalogo.txt')

catalog_strings = np.array([names, musical_style, solo_band_duo])
catalog_numbers = np.array([fans, likes, cash])
complete_catalog = Catalog(catalog_strings, catalog_numbers)

print(complete_catalog.mean_likes())
