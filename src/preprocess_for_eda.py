import pandas as pd
from raw_data_parser import ParseInputs

class PreprocessData(ParseInputs):
    """ Triming data from odds, serializing time to numerical representation """
    def __init__(self, data_path: str):
        super().__init__(data_path)
        
    def __trim_cols(self) -> pd.DataFrame:
        cols = ['div', 'date', 'time', 'hometeam', 'awayteam', 'fthg', 'ftag', 'ftr', 'hthg', 'htag', 'htr', 'referee', 'hs', 'as', 'hst', 'ast', 'hf', 'af', 'hc', 'ac', 'hy', 'ay', 'hr', 'ar', 'numerical_time']
        return self.data[cols]
        
    def __hours_to_numerical(self, x):
        hours = x[:1]
        mins = int(x[-1:]) * 100 / 60
        return float(hours + str(mins))
    
    def __convert_time(self) -> pd.DataFrame:
        self.data['numerical_time'] = self.data.apply(lambda x: self.__hours_to_numerical(x['time']), axis = 1)
        return self.data
    
    def prepare_for_eda(self) -> pd.DataFrame:
        self.data = self.parse_data().reset_index(drop = True)
        self.data = self.__convert_time()
        return self.__trim_cols()
    