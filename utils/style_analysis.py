from utils.ranking_analysis import Analysis


import numpy as np
import collections
from utils.functions import linha, linha2, menu_count_musical_style

class Style(Analysis):
    def __init__(self, strings, numbers) -> None:
        super().__init__(strings, numbers)

    def count_musical_style(self):
        #contagem de elementos que se repetem em um array
        musical_styles = self.strings[:, 1]
        count_musical_styles = collections.Counter(musical_styles)

        menu_count_musical_style()

        for key, value in count_musical_styles.items():
            print(f'{key:<40}', end=' ')
            print(value)
            print('\033[1;33m--\033[m'*28)
    
    def fans_per_style(self):
        styles = np.array(['MPB', 'Hiphop', 'Indie', 'Samba', 'Pop', 'Rock', 'Funk', 'Sertanejo'])
        musical_styles = self.strings[:, 1]
        musical_styles_index = np.argwhere(musical_styles == styles)

        return musical_styles[musical_styles_index]
        